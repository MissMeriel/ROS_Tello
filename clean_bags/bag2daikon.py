#/usr/bin/python
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
xml_topics = []
topics_in = []
topics_out = []

MY_MACRO = """
if testing:
	print test_output            
"""

FIELD_MACRO = """
if want_fields:
	print field_output
"""

def print_fields(field_output):
	exec FIELD_MACRO in globals(),locals()

def display_bag_info(bag_name):
	global topics, message_types, message_fields, bag_info
	#print "topics: "+str(bag.get_type_and_topic_info()[1].keys())
	bag_info = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_name], stdout=subprocess.PIPE).communicate()[0])
	bag_topics = bag_info['topics']
	keys = bag_info.keys()
	print("BAG INFO")
	for key in keys:
		print(key+str(": ")+str(bag_info[key]))
	#For every topic in the bag, display its fields.
	print_fields("\nFIELDS FOR "+str(len(bag_topics))+" TOPICS\n")
	#sys.stdout.write("\nFIELDS FOR %u TOPICS\n" % len(bag_topics))
	i = 0
	bag = rosbag.Bag(bag_name)
	print("bag_topics: "+str(bag_topics))
	for topic in bag_topics:
		message_fields.update({topic['type']: {}})
		message_types.append(topic['type'])
		topics.append(topic['topic'])
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
\

def test_print(test_output):
	#test_output="\nmessage_types:\n"+str(message_types)
	exec MY_MACRO in globals(), locals()


def traverse_msg_tree(val, levels, msg_type, key):
	global message_fields
	for level in levels:
		if isinstance(val, list):
			for v in val:
				if level in str(v):
					val = v
		if not isinstance(val, list):
			val = getattr(val, level)
		test_print("\n\tlevel: "+str(level)+"\n\tval: "+str(val)+"\n\ttype: "+str(message_fields[msg_type][key]['type']))
		'''if(testing):
			print("\n\tlevel: "+str(level))
			print("\tval: "+str(val))
			print("\ttype: "+str(message_fields[msg_type][key]['type']))'''
	return val


def enumerate_msg_fields(topic, msg, msg_type):
	global testing, message_fields
	field_string = ""
	keys = message_fields[msg_type].keys()
	test_print("\nPRINTING msg:\n"+str(msg) + "\n\nmsg keys for "+str(topic)+":\n"+str(keys))
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
		#print(str(val) + str(field['type']))
		if  "string" in str(message_fields[msg_type][key]['type']) or "str" in str(message_fields[msg_type][key]['type']):
			field_string += "\n\""+str(val)+"\""
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)
		field_string += "\n1"
	field_string += "\n"
	return field_string


def build_param_string(index):
	global topics_in, topics, message_types
	param_string = ""
	msg_type = ""
	#print("BUILD_PARAM_STRING")
	for t in topics_in:
		i = topics.index(t)
		msg_type = message_types[i]
		#print(str(t)+" "+str(msg_type))
		if len(topics_in) == 1:
			param_string += msg_type
		elif i == 0 and len(topics_in) > 1:
			param_string += msg_type +", "
		elif i == len(topics_in)-1:
			param_string += msg_type
		else:
			param_string += "\_"+ msg_type +", "
	return param_string


def main():
	global testing, topics, message_types, message_fields, bag_info
	global xml_topics, topics_in, topics_out
	start_time = time.time()

	#handle CL args
	bag = rosbag.Bag(sys.argv[1])
	output_filename=sys.argv[1].split(".")
	dtrace_filename=output_filename[0]+".dtrace"
	decls_filename=output_filename[0]+".decls"
	io_topics = {}
	if(len(sys.argv) == 3):
		tree = ET.parse(sys.argv[2])
		root = tree.getroot()
		print("XML INFO\n"+str(root.tag))
		#print(root.attrib)
		for child in root:
			io_topics[child.attrib['name']] = child.attrib
			print child.tag, child.attrib
			'''print type(child.attrib)
			print child.attrib['topics_in']
			print type(child.attrib['topics_in'])
			print child.attrib['topics_out']
			print type(child.attrib['topics_out'])'''
			topics_in = child.attrib['topics_in'].split(" ")
			print("topics_in: "+str(topics_in))
			xml_topics.extend(topics_in)
			topics_out = child.attrib['topics_out'].split(" ")
			xml_topics.extend(topics_out)
			print("topics_out: "+str(topics_out))
	print("XML TOPICS: \n"+str(xml_topics))
	print(""+str(io_topics))
	#get bag info
	print "displaying bag info..."
	display_bag_info(sys.argv[1])
	print("global topics: "+str(topics))
	print("message_types: "+str(message_types))
	print("message_fields: "+str(message_fields))

	#make decls file
	print "Writing decls to "+decls_filename
	decls_file=open(decls_filename, "w")
	decls_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n"
	decls_header += "\nppt ..main():::ENTER\n\tppt-type enter\n"
	decls_header += "\nppt ..main():::EXIT0\n\tppt-type subexit\n\tvariable return\n\t\tvar-kind variable\n\t\trep-type int\n\t\tdec-type int\n\t\tcomparability 1"
	decls_file.write(decls_header)
	index = 0
	for topic in topics:
		test_output = "\n"+str(topic)+"\n"+str(type(topic))
		exec MY_MACRO in globals(),locals()
		#topic=topic[1:len(topic)]
		function_name = topic.replace("/", "")
		enter_string = "\n\nppt .."+function_name+"("
		param_string = build_param_string(index)
		enter_string += param_string + "):::ENTER"
		#enter_string += "():::ENTER"
		enter_string += "\n\tppt-type enter"
		i = 0
		for t in topics_in:
			enter_string += "\n\tvariable a"+str(i)
			enter_string += "\n\t\tvar-kind variable"
			enter_string += "\n\t\trep-type hashcode"
			msg_type = message_types[index]
			enter_string += "\n\t\tdec-type "+ str(msg_type)
			enter_string += "\n\t\tflags is_param"
			keys = message_fields[msg_type].keys()
			for key in keys:
				field = message_fields[msg_type][key]
				enter_string += "\n\tvariable a"+str(i)+"."+key
				enter_string += "\n\t\tvar-kind field "+key
				enter_string += "\n\t\tenclosing-var a"+str(i)
				field_type = python_to_daikon_type(field['type'])
				enter_string += "\n\t\trep-type "+field_type
				enter_string += "\n\t\tdec-type "+field_type
				enter_string += "\n\t\tcomparability 1"
			i += 1
		enter_string += "\n"
		exit_string = "\nppt .."+function_name+"("+param_string+"):::EXIT0" + "\n\tppt-type subexit" + "\n\tvariable return" + "\n\t\tvar-kind variable" + "\n\t\trep-type hashcode" + "\n\t\tdec-type "+str(message_types[index]) + "\n\t\tcomparability 1"
		decls_file.write(enter_string)
		decls_file.write(exit_string)
		msg_type = message_types[index]
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
			field_string += "\n\t\tcomparability 1"
		decls_file.write(field_string+"\n")
		index += 1
	decls_file.close()

	#make dtrace file
	print "Writing dtrace to "+dtrace_filename
	test_print("\nmessage_types:\n"+str(message_types))
	dtrace_file=open(dtrace_filename, "w")
	dtrace_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n" + "\n..main():::ENTER\n" 
	dtrace_file.write(dtrace_header)
	call_counts=np.zeros(len(topics), dtype=int)
	msg_count = 0
	last_msgs = {}
	for topic, msg, t in bag.read_messages(xml_topics):
	#'''for topic, msg, t in bag.read_message(topics=sys.argv[2:len(sys.argv)]):'''
		if(msg):
			last_msgs[str(type(msg))] = {'msg': msg, 'hash': str(hex(id(msg)))}
			msg_count += 1
			print("Processing message "+str(msg_count)+" out of "+str(bag_info['messages']))
			sys.stdout.write("\033[F") # Cursor up one line
		index = topics.index(topic)
		topic=topic.replace("/", "")
		param_string = build_param_string(index)
		enter_string = "\n.."+topic+"("+param_string+"):::ENTER\nthis_invocation_nonce\n"+str(call_counts[index])
		i = 0
		for t in topics_in:
			index = topics.index(t)
			msg_type = message_types[index]
			last_msg = last_msgs[str(msg_type)]
			enter_string += "\na"+str(i)
			enter_string += "\n"+last_msg['hash']
			enter_string += "\n1"
			keys = message_fields[msg_type].keys()
			for key in keys:
				field = message_fields[msg_type][key]
				enter_string += "\nvariable a"+str(i)+"."+key
				enter_string += enumerate_msg_fields(topic, msg, msg_type)
				field_type = python_to_daikon_type(field['type'])
			i += 1
		enter_string += "\n"
		exit_string = "\n.."+topic+"("+param_string+"):::EXIT0\nthis_invocation_nonce\n"+str(call_counts[index])+"\nreturn"+"\n"+str(hex(id(msg)))+"\n1"
		#enumerate msg fields
		msg_type = message_types[index]
		field_string = enumerate_msg_fields(topic, msg, msg_type)
		dtrace_file.write(enter_string+exit_string+field_string)
		if (topic):
			call_counts[index] = call_counts[index] + 1
	dtrace_file.write("\n..main():::EXIT0\nreturn\n0\n1\n")
	dtrace_file.close()
	bag.close()
	print("Processed "+str(msg_count)+" out of "+str(bag_info['messages'])+" messages")
	print("----- %s seconds runtime -----" % (time.time() - start_time))



if __name__ == "__main__":
    # execute only if run as a script
    main()
