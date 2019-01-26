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
xml_topics = Set()
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
	global testing, message_fields
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
		if  "string" in str(message_fields[msg_type][key]['type']) or "str" in str(message_fields[msg_type][key]['type']):
			val = val.replace("\n", "")
			field_string += "\n\""+str(val)+"\""
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)
		field_string += "\n1"
	field_string += "\n"
	return field_string


def enumerate_param_msg_fields(topic, msg, msg_type, i):
	global message_fields
	field_string = ""
	keys = message_fields[msg_type].keys()
	#test_print("\nPRINTING msg:\n"+str(msg) + "\n\nmsg keys for "+str(topic)+":\n"+str(keys))
	for key in keys:
		field = message_fields[msg_type][key]
		field_string += "\nparam"+str(i)+"."+key
		levels = key.split(".")
		#test_print("\nRETRIEVING key: "+key+ "\nlevels: "+str(levels))
		if msg != None:
			val = traverse_msg_tree(msg, levels, msg_type, key)
		else:
			val = "nonsensical"
		if  "string" in str(message_fields[msg_type][key]['type']) or "str" in str(message_fields[msg_type][key]['type']):
			val = val.replace("\n", "")
			field_string += "\n\""+str(val)+"\"\n1"
		else:
			val = python_to_daikon_literal(val)
			field_string += "\n"+str(val)+"\n1"
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
	global xml_topics, topics_in, topics_out
	start_time = time.time()

	#handle CL args
	bag = rosbag.Bag(sys.argv[1])
	output_filename=sys.argv[1].split(".")
	dtrace_filename=output_filename[0]+".dtrace"
	decls_filename=output_filename[0]+".decls"
	io_topics = {}
	node_lookup = {}
	if(len(sys.argv) == 3):
		tree = ET.parse(sys.argv[2])
		root = tree.getroot()
		test_print("XML INFO")
		topics_in = []
		topics_out = []
		for child in root:
			#print child.tag, child.attrib
			io_topics[child.attrib['name']] = child.attrib
			topics_in = filter(None, child.attrib['topics_in'].split(" "))
			xml_topics.update(topics_in)
			topics_out = filter(None, child.attrib['topics_out'].split(" "))
			xml_topics.update(topics_out)
			io_topics[child.attrib['name']]['topics_in'] = topics_in
			io_topics[child.attrib['name']]['topics_out'] = topics_out
	for t in xml_topics:
		node_lookup[t] = {'in': "", 'out': ""}
	test_print("BIULDING NODE LOOKUP")
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
	print "displaying bag info..."
	display_bag_info(sys.argv[1])
	test_print("GLOBAL topics: \n"+str(topics))
	test_print("MESSAGE_TYPES: \n"+str(message_types))
	#test_print("MESSAGE_FIELDS: \n"+str(message_fields))

	#make decls file
	print "Writing decls to "+decls_filename
	decls_file=open(decls_filename, "w")
	decls_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n"
	decls_header += "\nppt ..main():::ENTER\n\tppt-type enter\n"
	decls_header += "\nppt ..main():::EXIT0\n\tppt-type subexit\n\tvariable return\n\t\tvar-kind variable\n\t\trep-type int\n\t\tdec-type int\n\t\tcomparability 1\n"
	decls_file.write(decls_header)
	index = 0
	test_print("TOPICS:\n"+str(topics)+"\n")
	for topic in topics:
		test_print("WRITING DECL FOR "+str(topic)+"\n"+str(type(topic)))
		slashed_topic = topic
		#get node publishing that topic
		test_print("node_lookup["+slashed_topic+"]['out']: "+str(node_lookup[slashed_topic]['out']))
		node_name = node_lookup[slashed_topic]['out']
		if node_name == '':
			topics_in = []
		else:
		#get topics consumed by that node for the fxn signature's params
			topics_in = io_topics[node_name]['topics_in']
		
		test_print("TOPICS_IN FOR "+node_name+":"+str(topics_in))
		function_name = topic.replace("/", "")
		enter_string = "\nppt .."+function_name+"("
		signature_param_string = build_param_string(topics_in)
		enter_string += signature_param_string + "):::ENTER"
		enter_string += "\n\tppt-type enter"
		i = 0
		param_string = ""
		for t in topics_in:
			topic_index = topics.index(t)
			param_string += "\n\tvariable param"+str(i)
			param_string += "\n\t\tvar-kind variable"
			param_string += "\n\t\trep-type hashcode"
			msg_type = message_types[topic_index]
			param_string += "\n\t\tdec-type "+ str(msg_type)
			param_string += "\n\t\tflags is_param"
			keys = message_fields[msg_type].keys()
			for key in keys:
				field = message_fields[msg_type][key]
				param_string += "\n\tvariable param"+str(i)+"."+key
				param_string += "\n\t\tvar-kind field "+key
				param_string += "\n\t\tenclosing-var param"+str(i)
				field_type = python_to_daikon_type(field['type'])
				param_string += "\n\t\trep-type "+field_type
				param_string += "\n\t\tdec-type "+field_type
				param_string += "\n\t\tcomparability 1"
			i += 1
		enter_string += param_string+ "\n"
		exit_string = "\nppt .."+function_name+"("+signature_param_string+"):::EXIT0" + "\n\tppt-type subexit" + param_string +"\n\tvariable return" + "\n\t\tvar-kind variable" + "\n\t\trep-type hashcode" + "\n\t\tdec-type "+str(message_types[index]) + "\n\t\tcomparability 1"
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
	dtrace_file=open(dtrace_filename, "w")
	dtrace_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n" + "\n..main():::ENTER\n" 
	dtrace_file.write(dtrace_header)
	call_counts=np.zeros(len(topics), dtype=int)
	msg_count = 0
	last_msgs = {}
	for t in topics:
		last_msgs[t] = None
	for topic, msg, t in bag.read_messages(xml_topics):
		if(msg):
			index = topics.index(topic)
			msg_type = message_types[index]
			last_msgs[topic] = {'msg': msg, 'hash': str(hex(id(msg))), 'topic': topic}
			msg_count += 1
			print("Processing message "+str(msg_count)+" out of "+str(bag_info['messages']))
			if not testing:
				sys.stdout.write("\033[F") # Cursor up one line
		index = topics.index(topic)
		slashed_topic = topic
		topic=topic.replace("/", "")
		#test_print("node_lookup["+slashed_topic+"]['out']: "+str(node_lookup[slashed_topic]['out']))
		node_name = node_lookup[slashed_topic]['out']
		if node_name == '':
			topics_in = []
		else:
			topics_in = io_topics[node_name]['topics_in']
		#test_print("TOPICS_IN FOR "+node_name+": "+str(topics_in))
		signature_param_string = build_param_string(topics_in)
		#test_print("signature_param_string: "+signature_param_string)
		#build ENTER and EXIT strings
		enter_string = "\n.."+topic+"("+signature_param_string+"):::ENTER\nthis_invocation_nonce\n"+str(call_counts[index])
		exit_string = exit_string = "\n.."+topic+"("+signature_param_string+"):::EXIT0\nthis_invocation_nonce\n"+str(call_counts[index])
		i = 0
		param_string = ""
		#test_print("LAST_MSGS:\n"+str(last_msgs))
		for t in topics_in:
			#t = t.replace("/", "")
			param_topic_index = topics.index(t)
			msg_type = message_types[param_topic_index]
			last_msg = last_msgs[t]
			if last_msg != None:
				param_string += "\nparam"+str(i) + "\n"+last_msg['hash'] + "\n1"
				message = last_msg['msg']
			else:
				param_string += "\nparam"+str(i) + "\n"+hex(id("")) + "\n1"
				message = None
			keys = message_fields[msg_type].keys()
			#test_print("\nFields for "+str(message_fields[msg_type])+"\nKeys:\n"+str(keys))
			param_string += enumerate_param_msg_fields(t, message, msg_type, i)
			i += 1
		enter_string += param_string + "\n"
		exit_string += param_string
		#enumerate EXIT return msg fields
		msg_type = message_types[index]
		exit_string += "\nreturn"+"\n"+str(hex(id(msg)))+"\n1"
		exit_string += enumerate_msg_fields(topic, msg, msg_type)
		dtrace_file.write(enter_string+exit_string)
		if (topic):
			call_counts[index] = call_counts[index] + 1
		#time.sleep(2)
	dtrace_file.write("\n..main():::EXIT0\nreturn\n0\n1\n")
	dtrace_file.close()
	bag.close()
	print("Processed "+str(msg_count)+" out of "+str(bag_info['messages'])+" messages")
	print("----- %s seconds runtime -----" % (time.time() - start_time))



if __name__ == "__main__":
    # execute only if run as a script
    main()