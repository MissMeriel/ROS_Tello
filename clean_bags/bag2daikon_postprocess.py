#/usr/bin/python
from __future__ import print_function
import sys
import time
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml
import xml.etree.ElementTree as ET


# Pass in: 	invariant xml
#		bagfile
# Generating: 	conditionals splitter file (.spinfo)
#		temporals .decls and .dtrace


topics = []
message_types = []
message_fields = {}
bag_info = {}
testing = False
want_fields = False
xml_topics = Set()
comparability_count = 1
comparability_map = {}
xml_file = ""


MY_MACRO = """
if testing:
	print(test_output)
"""

FIELD_MACRO = """
if want_fields:
	print(field_output)
"""

def print_fields(field_output):
	exec FIELD_MACRO in globals(),locals()


def display_bag_info(bag_name):
	global topics, message_types, message_fields, bag_info
	#print "topics: "+str(bag.get_type_and_topic_info()[1].keys())
	bag_info = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_name], stdout=subprocess.PIPE).communicate()[0])
	bag_topics = bag_info['topics']
	keys = bag_info.keys()
	test_print("BAG INFO")
	for key in keys:
		test_print(key+str(": ")+str(bag_info[key]))
	#For every topic in the bag, display its fields.
	print_fields("\nFIELDS FOR "+str(len(bag_topics))+" TOPICS\n")
	#sys.stdout.write("\nFIELDS FOR %u TOPICS\n" % len(bag_topics))
	i = 0
	bag = rosbag.Bag(bag_name)
	test_print("bag_topics: "+str(bag_topics))
	for t in topics:
		for topic in bag_topics:
			if topic['topic'] == t:
				message_fields.update({topic['type']: {}})
				message_types.append(topic['type'])
				#topics.append(topic['topic'])
				for _, msg, _ in bag.read_messages(topics=topic['topic']):
					print_topic_fields(topic['topic'], "",  msg, 0, i, topic['type'])
					print_fields('')
					break
				i += 1
	bag.close()


def print_topic_fields(field_name, path, msg, depth, index, msg_type):
	global message_types, message_fields
	if hasattr(msg, '__slots__'):
		print_fields(' ' * (depth * 2) + field_name)
		for slot in msg.__slots__:
			if(path != ""):
				new_path = path+"."+slot
			else:
				new_path = slot
			print_topic_fields(slot, new_path, getattr(msg, slot), depth + 1, index, msg_type)
	elif isinstance(msg, list):
		if (len(msg) > 0) and hasattr(msg[0], '__slots__'):
		    print_fields(' ' * (depth * 2) + field_name + '[]')
		    for slot in msg[0].__slots__:
			if(path != ""):
				new_path = path+"."+slot
			else:
				new_path = slot
			print_topic_fields(slot, new_path, getattr(msg[0], slot), depth + 1, index, msg_type)
	else:
		print_fields(' ' * (depth * 2) + field_name)
		print_fields(' ' * (depth * 2) + "path: "+path)
		print_fields(' ' * (depth * 2) + "type: "+str(type(msg)))
		print_fields(' ' * (depth * 2) + "addr: "+str(hex(id(msg))))
		message_fields[msg_type][path] = {'name': field_name, 'type': type(msg), 'addr': hex(id(msg))}


def python_to_daikon_type(python_type):
	field_type = str(python_type).split("\'")[1]
	if(field_type == "str"):
		field_type = "string"
	if(field_type == "bool"):
		field_type = "boolean"
	return field_type;


def python_to_daikon_literal(python_lit):
	python_lit = str(python_lit)
	if(python_lit == "True"):
		daikon_lit = "0"
	elif(python_lit == "False"):
		daikon_lit = "1"
	else:
		daikon_lit = python_lit
	return daikon_lit


def test_print(test_output):
	exec MY_MACRO in globals(), locals()


def parse_xml(tree):
	global xml_topics
	root = tree.getroot()
	test_print("XML INFO")
	topics_in = []
	topics_out = []
	for child in root:
		#print(child.tag+"="+child.attrib)
		io_topics[child.attrib['name']] = child.attrib
		topics_in = filter(None, child.attrib['topics_in'].split(" "))
		xml_topics.update(topics_in)
		topics_out = filter(None, child.attrib['topics_out'].split(" "))
		xml_topics.update(topics_out)
		io_topics[child.attrib['name']]['topics_in'] = topics_in
		io_topics[child.attrib['name']]['topics_out'] = topics_out
	for t in xml_topics:
		node_lookup[t] = {'in': "", 'out': ""}
	test_print("BUILDING NODE LOOKUP")
	for node in io_topics:
		for ti in io_topics[node]['topics_in']:
			test_print("node: "+str(node)+"; ti: "+str(ti))
			node_lookup[ti]['in']=node
		for to in io_topics[node]['topics_out']:
			test_print("node: "+str(node)+"; to: "+str(to))
			node_lookup[to]['out']=node
		test_print(node_lookup)
	test_print("XML TOPICS: \n"+str(xml_topics))
	test_print("IO_TOPICS:")
	for t in io_topics:
		test_print(t+": "+str(io_topics[t]))
	test_print("NODE_LOOKUP:")
	for t in node_lookup:
		test_print(t+": "+str(node_lookup[t]))
	topics = []
	for t in xml_topics:
		if t != '':
			topics.append(t)


def parse_inv_xml(xml_tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for child in root.iter("PPT"):
		for invinfo in child.iter("INVINFO"):
			if("OneOf" in invinfo.find("DAIKONCLASS").text and "one of" in invinfo.find("INV").text):
				test_print(child.find("PPTNAME").text)
				test_print("\t"*1 + str(invinfo.tag)+"="+str(invinfo.attrib))
				test_print("\t"*2+"PARENT="+invinfo.find("PARENT").text)
				test_print("\t"*2+"INV="+invinfo.find("INV").text)
				test_print("\t"*2+"SAMPLES="+invinfo.find("SAMPLES").text)
				test_print("\t"*2+"DAIKON="+invinfo.find("DAIKON").text)
				test_print("\t"*2+"DAIKONCLASS="+invinfo.find("DAIKONCLASS").text)
				test_print("\t"*2+"METHOD="+invinfo.find("METHOD").text)
				if("one of" in invinfo.find("INV").text):
					ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
					test_print("ppt "+str(ppt))
					spinfo_string += "PPT_NAME "+ ppt
					infosplit = invinfo.find("INV").text.split("one of")
					varname = infosplit[0]
					valsplit = infosplit[1].replace("{", "").strip("}")
					test_print(valsplit)
					vals = valsplit.split(",")
					for val in vals:
						spinfo_string += "\n"+varname+" == "+val
					spinfo_string += "\n\n"
	print("SPINFO_STRING:")
	print(spinfo_string)
	return spinfo_string


def main():
	global testing, topics, message_types, message_fields, bag_info
	global comparability_map, comparability_count
	start_time = time.time()

	#handle CL args
	bag = rosbag.Bag(sys.argv[1])
	output_filename=sys.argv[1].split(".")
	spinfo_filename=output_filename[0]+".spinfo"

	#process .inv xml
	if(len(sys.argv) == 3):
		xml_tree = ET.parse(sys.argv[2])
		spinfo_string = parse_inv_xml(xml_tree)
		spinfo_file = file(spinfo_filename, "w")
		spinfo_file.write(spinfo_string)
		spinfo_file.close()
		print("New .spinfo file: "+spinfo_filename)
		print("Run .spinfo file as: java -cp $DAIKONDIR/daikon.jar daikon.Daikon --config_option daikon.derive.Derivation.disable_derived_variables=true "+ output_filename[0]+".decls "+ output_filename[0]+".dtrace "+spinfo_filename)
		

if __name__ == "__main__":
    # execute only if run as a script
    main()
