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
				for _, msg, _ in bag.read_messages(topics=topic['topic']):
					print_topic_fields(topic['topic'], "",  msg, 0, i, topic['type'])
					print_fields('')
					break
				i += 1
	bag.close()
	test_print("MESSAGE_FIELDS AFTER DISPLAY BAG: \n"+str(message_fields))


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

def traverse_msg_tree(val, levels, msg_type, key):
	global message_fields
	for level in levels:
		#test_print("\nGetting attribute for "+str(val)+", "+str(level))
		if isinstance(val, list):
			for v in val:
				if level in str(v):
					val = v
		if not isinstance(val, list):
			val = getattr(val, level)
		#test_print("\n\tlevel: "+str(level)+"\n\tval: "+str(val)+"\n\ttype: "+str(message_fields[msg_type][key]['type']))
	return val


def enumerate_msg_fields(topic, msg, msg_type):
	global testing, message_fields, comparability_map, comparability_count
	field_string = ""
	keys = message_fields[msg_type].keys()
	test_print("\nPRINTING msg:\n"+str(msg) + "\nmsg keys for "+str(topic)+":\n"+str(keys))
	'''if(testing):
		print("\nPRINTING msg:\n"+str(msg))
		print("\nmsg keys for "+str(topic)+":\n"+str(keys))'''
	for key in keys:
		field = message_fields[msg_type][key]
		field_string += "\nreturn."+key
		levels = key.split(".")
		#TODO: profile mem/bandwidth/wall clock time for test_print vs if(testing)
		test_print("\nRETRIEVING key: "+key+ "\nlevels: "+str(levels))
		'''if(testing):
			print("\nRETRIEVING key: "+key)
		if(testing):
			print("levels: "+str(levels))'''

		val = traverse_msg_tree(msg, levels, msg_type, key)
		test_print(str(val) + str(field['type']))
		field_type = message_fields[msg_type][key]['type']
		#using actual type of field_type
		comparability_int = 1 #get_comparability_int(key, field_type)
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
		comparability_int = 1 #get_comparability_int(key, field_type)
		if  "string" in str(field_type) or "str" in str(field_type):
			#and val != "nonsensical":
			val = val.replace("\n", "")
			field_string += "\n\""+str(val)+"\""
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)
		field_string += "\n"+str(comparability_int)
	return field_string


def get_comparability_int(field, field_type):
	global comparability_count, comparability_map
	#print("GET COMPARABILITY INT FOR field:"+str(field)+", field_type:"+str(field_type), end='')
	if "rotation" in field:
		try:
			comparability_int = comparability_map["rotation"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["rotation"] = comparability_count
	elif "angular" in field:
		try:
			comparability_int = comparability_map["angular"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["angular"] = comparability_count
	elif "translation" in field:
		try:
			comparability_int = comparability_map["translation"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["translation"] = comparability_count
	elif "frame_id" in field:
		# allows for comparison of frame_id and child_frame_id
		try:
			comparability_int = comparability_map["frame_id"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["frame_id"] = comparability_count
	elif "stamp.nsecs" in field:
		try:
			comparability_int = comparability_map["stamp.nsecs"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["stamp.nsecs"] = comparability_count
	elif "stamp.secs" in field:
		try:
			comparability_int = comparability_map["stamp.secs"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["stamp.secs"] = comparability_count
	elif "header.seq" in field:
		try:
			comparability_int = comparability_map["header.seq"]
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map["header.seq"] = comparability_count
	else:
		try:
			comparability_int = comparability_map[field_type]
			
		except:
			comparability_count += 1
			comparability_int = comparability_count
			comparability_map[field_type] = comparability_count
	#print(", comparability_int:"+str(comparability_int))
	return comparability_int


def build_param_string(topics_in):
	global topics, message_types
	param_string = ""
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


def process_xml(xml_tree):
	global xml_topics, topics
	io_topics = {}
	node_lookup = {}
	root = xml_tree.getroot()
	test_print("XML INFO")
	topics_in = []
	topics_out = []
	for child in root:
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
	topics = []
	for t in xml_topics:
		if t != '':
			topics.append(t)
	test_print("XML TOPICS: \n"+str(xml_topics))
	test_print("IO_TOPICS:")
	for t in io_topics:
		test_print(t+": "+str(io_topics[t]))
	test_print("NODE_LOOKUP:")
	for t in node_lookup:
		test_print(t+": "+str(node_lookup[t]))


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


	#process xml file
	if(len(sys.argv) == 3):
		tree = ET.parse(sys.argv[2])
		process_xml(tree)

	#get bag info
	test_print("displaying bag info...")
	display_bag_info(sys.argv[1])
	test_print("GLOBAL topics: \n"+str(topics))
	test_print("MESSAGE_TYPES: \n"+str(message_types))
	test_print("MESSAGE_FIELDS: \n"+str(message_fields))

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
	temporals = ["next"] #, "eventually", "until"]
	topics_copy = np.copy(topics)
	for temporal in temporals:
		for topic in topics:
			test_print("WRITING DECL FOR "+str(topic)+" "+str(temporal))
			function_name = topic +"_"+temporal
			signature_param_string = ""
			enter_string = "\nppt .."+function_name+"("+signature_param_string+"):::ENTER"
			enter_string += "\n\tppt-type enter"
			param_string = ""

			enter_string += param_string+ "\n"
			decls_file.write(enter_string)
			
			topic_index = 0
			exit_count = 0
			for topic1 in topics_copy:
				test_print("WRITING SUBEXIT FOR "+topic+" RETURNING "+topic1)
				exit_string = "\nppt .."+function_name+"("+signature_param_string+"):::EXIT"+str(topic_index) 
				exit_string += "\n\tppt-type subexit" + param_string 
				exit_string += "\n\tvariable return" 
				exit_string += "\n\t\tvar-kind variable" 
				exit_string += "\n\t\trep-type hashcode"
				exit_string += "\n\t\tdec-type "+str(message_types[topic_index])
				exit_string += "\n\t\tcomparability 1"
				msg_type = message_types[topic_index]
				keys = message_fields[msg_type].keys()
				field_string = ""
				for key in keys:
					field = message_fields[msg_type][key]
					field_string += "\n\tvariable return."+key
					field_string += "\n\t\tvar-kind field "+field['name']
					field_string += "\n\t\tenclosing-var return"
					field_type = python_to_daikon_type(field['type'])
					field_string += "\n\t\trep-type "+field_type
					field_string += "\n\t\tdec-type "+field_type
					comparability_int = 1 #get_comparability_int(key, field['type'])
					field_string += "\n\t\tcomparability "+str(comparability_int)
				exit_string += (field_string+"\n")
				decls_file.write(exit_string+"\n")
				topic_index += 1
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
	logic_operators = {"next":{"topic":None, "msg":None, "type":None}, "eventually":{"topic":None, "msg":None, "type":None}, "until":{"topic":None, "msg":None, "type":None}, "always":{"topic":None, "msg":None, "type":None}}
	#last_topic = None
	last_msg = None
	for topic, msg, t in bag.read_messages(xml_topics):
		for temporal in temporals:
			if(msg):
				msg_count += 1
				#print("Processing message "+str(msg_count)+" out of "+str(bag_info['messages']))
				#sys.stdout.write("\033[F") # Cursor up one line
			if(logic_operators["next"]["topic"] != None and temporal == "next"):
				last_topic = logic_operators["next"]["topic"]
				signature_param_string = ""
				call_count = call_counts[last_topic]
				#build ENTER string
				enter_string = "\n.."+last_topic+"_next"+"("+signature_param_string+"):::ENTER"
				enter_string += "\nthis_invocation_nonce\n"+str(call_count)
				#build EXIT string
				exit_index = topics.index(topic)
				exit_string = "\n.."+last_topic+"_next"+"("+signature_param_string+"):::EXIT"+str(exit_index)
				exit_string += "\nthis_invocation_nonce\n"+str(call_count)
				#build ENTER/EXIT param string
				enter_param_string = ""
				enter_string += enter_param_string + "\n"

				exit_param_string = ""
				#build return string
				exit_string += "\nreturn"+"\n"+str(hex(id(msg)))+"\n1"
				msg_type = message_types[topics.index(topic)]
				keys = message_fields[msg_type].keys()
				field_string = ""
				exit_string += enumerate_msg_fields(topic, msg, msg_type)
				dtrace_file.write(enter_string+exit_string)
				#dtrace_file.write(enter_string+exit_string)
				call_counts[last_topic] = call_count + 1
			#last_topic = topic
			if(msg):
				#last_msg = msg
				msg_type = message_types[topics.index(topic)]
				logic_operators["next"] = {"topic": topic, "msg":msg, "type":msg_type}
				test_print("\nADDED "+topic+" "+str(msg)+"\n"+msg_type+" to NEXT in LOGIC_OPERATORS")
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