#/usr/bin/python
from __future__ import print_function
import sys
import time
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml
import xml.etree.ElementTree as ET



topics = []
message_types = []
message_fields = {}
bag_info = {}
testing = False
want_fields = False
xml_topics = Set()
comparability_count = 1
comparability_map = {}

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
	bag = rosbag.Bag(sys.argv[1])
	test_print("topics: "+str(bag.get_type_and_topic_info()[1].keys()))
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
					print_fields('')
					break
				i += 1
	bag.close()



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


def enumerate_msg_fields(topic, msg, msg_type):
	global testing, message_fields, comparability_map, comparability_count
	field_string = ""
	keys = message_fields[msg_type].keys()
	#test_print("\nPRINTING msg:\n"+str(msg) + "\n\nmsg keys for "+str(topic)+":\n"+str(keys))
	'''if(testing):
		print("\nPRINTING msg:\n"+str(msg))
		print("\nmsg keys for "+str(topic)+":\n"+str(keys))'''
	for key in keys:
		field = message_fields[msg_type][key]
		field_string += "\nreturn."+key
		levels = key.split(".")
		#TODO: profile mem/bandwidth/wall clock time for test_print vs if(testing)
		#test_print("\nRETRIEVING key: "+key+ "\nlevels: "+str(levels))
		'''if(testing):
			print("\nRETRIEVING key: "+key)
		if(testing):
			print("levels: "+str(levels))'''

		val = traverse_msg_tree(msg, levels, msg_type, key)
		#print(str(val) + str(field['type']))
		field_type = message_fields[msg_type][key]['type']
		#using actual type of field_type
		comparability_int = 1 ###get_comparability_int(key, field_type)
		if  "string" in str(field_type) or "str" in str(field_type):
			val = val.replace("\n", "")
			field_string += "\n\""+str(val)+"\""
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)
		field_string += "\n"+str(comparability_int)
	field_string += "\n"
	return field_string


def enumerate_param_msg_fields(topic, msg, msg_type, i):
	global message_fields
	field_string = ""
	keys = message_fields[msg_type].keys()
	test_print("\nPRINTING msg:\n"+str(msg))
	#test_print("\nmsg keys for "+str(topic)+":\n"+str(keys))
	for key in keys:
		val = ""
		field = message_fields[msg_type][key]
		field_string += "\nparam"+str(i)+"."+key
		levels = key.split(".")
		test_print("\nRETRIEVING key: "+key)
		#test_print("levels: "+str(levels))
		if msg != None:
			val = traverse_msg_tree(msg, levels, msg_type, key)
		else:
			val = "nonsensical"
			if(topic == '/state'):
				exit()
		#using actual type of field_type
		field_type = message_fields[msg_type][key]['type']
		comparability_int = 1 ###get_comparability_int(key, field_type)
		if  "string" in str(field_type) or "str" in str(field_type):
			#and val != "nonsensical":
			val = val.replace("\n", "")
			field_string += "\n\""+str(val)+"\""
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)
		field_string += "\n"+str(comparability_int)
	return field_string


def build_param_string(topics_in):
	global topics, message_types
	param_string = ""
	msg_type = ""
	#print("BUILDING PARAM STRING")
	#print("TOPICS_IN: "+str(topics_in))
	#print("MESSAGE_TYPES: "+str(message_types))
	i = 0
	for t in topics_in:
		index = topics.index(t)
		msg_type = message_types[index]
		if len(topics_in) == 1:
			param_string += msg_type
		elif i == 0 and len(topics_in) > 1:
			param_string += msg_type +","
		elif i == len(topics_in)-1:
			param_string += "\_" + msg_type
		else:
			param_string += "\_"+ msg_type +","
		i += 1
	return param_string


def main():
	global testing, topics, message_types, message_fields, bag_info
	global xml_topics
	global comparability_map, comparability_count
	start_time = time.time()

	#handle CL args
	bag = rosbag.Bag(sys.argv[1])
	output_filename=sys.argv[1].split(".")
	dtrace_filename=output_filename[0]+"_temporals.dtrace"
	decls_filename=output_filename[0]+"_temporals.decls"
	io_topics = {}
	node_lookup = {}
	#process xml file
	if(len(sys.argv) == 3):
		tree = ET.parse(sys.argv[2])
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

	#get bag info
	test_print("displaying bag info...")
	display_bag_info(sys.argv[1])
	test_print("GLOBAL topics: \n"+str(topics))
	#test_print("MESSAGE_TYPES: \n"+str(message_types))
	#test_print("MESSAGE_FIELDS: \n"+str(message_fields))

	#make decls file
	print("Writing decls to "+decls_filename+"...")
	decls_file=open(decls_filename, "w")
	decls_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n"
	decls_header += "\nppt ..main():::ENTER\n\tppt-type enter\n"
	decls_header += "\nppt ..main():::EXIT0\n\tppt-type subexit\n\tvariable return\n\t\tvar-kind variable\n\t\trep-type int\n\t\tdec-type int\n\t\tcomparability 1\n"
	decls_file.write(decls_header)
	index = 0
	comparability_count = 1
	comparability_map = {}
	temporals = ["next", "eventually", "until"]
	for temporal in temporals:
		for topic in topics:
			test_print("WRITING DECL FOR "+str(topic)+" "+str(temporal))
			function_name = topic +"_"+temporal
			#function_name = temporal
			signature_param_string = "string"
			enter_string = "\nppt .."+function_name+"("+signature_param_string+"):::ENTER"
			enter_string += "\n\tppt-type enter"
			param_string = ""
			param_string += "\n\tvariable topic_preceding"
			param_string += "\n\t\tvar-kind variable"
			param_string += "\n\t\trep-type string"
			param_string += "\n\t\tdec-type string"
			param_string += "\n\t\tflags is_param"
			param_string += "\n\t\tcomparability "+str(1)

			enter_string += param_string+ "\n"
			exit_string = "\nppt .."+function_name+"("+signature_param_string+"):::EXIT0" 
			exit_string += "\n\tppt-type subexit" + param_string 
			exit_string += "\n\tvariable return" 
			exit_string += "\n\t\tvar-kind variable"
			exit_string += "\n\t\trep-type string"
			exit_string += "\n\t\tdec-type string"
			exit_string += "\n\t\tcomparability 1"
			decls_file.write(enter_string)
			decls_file.write(exit_string+"\n")
			index += 1
	decls_file.close()
	test_print("\n")

	#make dtrace file
	print("Writing dtrace to "+dtrace_filename+"...")
	dtrace_file=open(dtrace_filename, "w")
	#write dtrace header
	dtrace_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n" + "\n..main():::ENTER\n" 
	dtrace_file.write(dtrace_header)
	#call_counts=1
	call_counts={}
	for topic in topics:
		call_counts[topic] = 1
	msg_count = 0
	last_topic = None
	current_topic = None
	for topic, msg, t in bag.read_messages(xml_topics):
		if(msg):
			msg_count += 1
			print("Processing message "+str(msg_count)+" out of "+str(bag_info['messages']))
			sys.stdout.write("\033[F") # Cursor up one line
		current_topic = topic
		if(last_topic != None):
			signature_param_string = "string"
			call_count = call_counts[last_topic]
			#build ENTER string
			enter_string = "\n.."+last_topic+"_next"+"(string):::ENTER"
			#enter_string = "\n..next"+"(string):::ENTER"
			enter_string += "\nthis_invocation_nonce\n"+str(call_count)
			#build EXIT string
			exit_string = "\n.."+last_topic+"_next"+"("+signature_param_string+"):::EXIT0"
			#exit_string = "\n..next"+"("+signature_param_string+"):::EXIT0"
			exit_string += "\nthis_invocation_nonce\n"+str(call_count)
			#build ENTER/EXIT param string
			param_string = ""
			enter_param_string = ""
			enter_param_string += "\ntopic_preceding"
			enter_param_string += "\n\""+last_topic+"\""
			enter_param_string += "\n1"
			exit_param_string = enter_param_string

			enter_string += enter_param_string + "\n"
			exit_string += exit_param_string
			exit_string += "\nreturn"+"\n\""+topic+"\"\n1\n"
			dtrace_file.write(enter_string+exit_string)
			call_counts[last_topic] = call_count + 1

		last_topic = current_topic

	#write dtrace EOF
	dtrace_file.write("\n..main():::EXIT0\nreturn\n0\n1\n")
	dtrace_file.close()
	bag.close()

	for key in call_counts.keys():
		print(key + ": "+ str(call_counts[key]))
	print("Processed "+str(msg_count)+" out of "+str(bag_info['messages'])+" messages")
	print("Output: "+decls_filename+" "+dtrace_filename)
	print("----- %s seconds runtime -----" % (time.time() - start_time))



if __name__ == "__main__":
    # execute only if run as a script
    main()
