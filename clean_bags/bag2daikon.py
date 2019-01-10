#/usr/bin/python
import sys
import time
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml

topics = []
message_types = []
message_fields = {}
bag_info = {}
testing = False


MY_MACRO = """
if testing:
	print test_output            
"""


def display_bag_info(bag_name):
	global topics, message_types, message_fields, bag_info
	#print "topics: "+str(bag.get_type_and_topic_info()[1].keys())
	bag_info = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_name], stdout=subprocess.PIPE).communicate()[0])
	bag_topics = bag_info['topics']
	print("BAG INFO")
	keys = bag_info.keys()
	for key in keys:
		print(key+str(": ")+str(bag_info[key]))
	bag = rosbag.Bag(bag_name)
	#For every topic in the bag, display its fields.
	sys.stdout.write("\nFIELDS FOR %u TOPICS\n" % len(bag_topics))
	i = 0
	for topic in bag_topics:
		message_fields.update({topic['type']: {}})
		message_types.append(topic['type'])
		topics.append(topic['topic'])
		for _, msg, _ in bag.read_messages(topics=topic['topic']):
			print_topic_fields(topic['topic'], "",  msg, 0, i, topic['type'])
			print('')
			break
		i += 1
	bag.close()


def print_topic_fields(field_name, path, msg, depth, index, msg_type):
	global message_types, message_fields
	if hasattr(msg, '__slots__'):
		print(' ' * (depth * 2) + field_name)
		for slot in msg.__slots__:
			if(path != ""):
				new_path = path+"."+slot
			else:
				new_path = slot
			print_topic_fields(slot, new_path, getattr(msg, slot), depth + 1, index, msg_type)
	elif isinstance(msg, list):
		if (len(msg) > 0) and hasattr(msg[0], '__slots__'):
		    print(' ' * (depth * 2) + field_name + '[]')
		    for slot in msg[0].__slots__:
			if(path != ""):
				new_path = path+"."+slot
			else:
				new_path = slot
			print_topic_fields(slot, new_path, getattr(msg[0], slot), depth + 1, index, msg_type)
	else:
		print(' ' * (depth * 2) + field_name)
		print(' ' * (depth * 2) + "path: "+path)
		print(' ' * (depth * 2) + "type: "+str(type(msg)))
		print(' ' * (depth * 2) + "addr: "+str(hex(id(msg))))
		message_fields[msg_type][path] = {'name': field_name, 'type': type(msg), 'addr': hex(id(msg))}


def python_to_daikon_type(python_type):
	field_type = str(python_type).split("\'")[1]
	if(field_type == "str"):
		field_type = "string"
	if(field_type == "bool"):
		field_type = "boolean"
	return field_type;


def enumerate_msg_fields(topic, msg, msg_type):
	global testing, message_fields
	field_string = ""
	keys = message_fields[msg_type].keys()
	test_output = "\nPRINTING msg:\n"+str(msg) + "\n\nmsg keys for "+str(topic)+":\n"+str(keys)
	exec MY_MACRO in globals(),locals()
	'''if(testing):
		print("\nPRINTING msg:\n"+str(msg))
		print("\nmsg keys for "+str(topic)+":\n"+str(keys))'''
	for key in keys:
		field = message_fields[msg_type][key]
		field_string += "\nreturn."+key
		levels = key.split(".")

		'''if(testing):
			print("\nRETRIEVING key: "+key)
		if(testing):
			print("levels: "+str(levels))'''
		test_output = "\nRETRIEVING key: "+key + "\nlevels: "+str(levels)
		exec MY_MACRO in globals(),locals()

		val = msg
		for level in levels:
			if isinstance(val, list):
				for v in val:
					if level in str(v):
						val = v
			if not isinstance(val, list):
				val = getattr(val, level)
			if(testing):
				print("\tlevel: "+str(level))
				print("\tval: "+str(val))
				print("\ttype: "+str(message_fields[msg_type][key]['type']))
		if message_fields[msg_type][key]['type'] == "string" or message_fields[msg_type][key]['type'] == "str":
			field_string += "\n\""+str(val)+"\""
		else:
			field_string += "\n"+str(val)
		field_string += "\n1"
	field_string += "\n"
	return field_string


def main():
	global testing, topics, message_types, message_fields, bag_info
	start_time = time.time()
	bag = rosbag.Bag(sys.argv[1])
	output_filename=sys.argv[1].split(".")
	dtrace_filename=output_filename[0]+".dtrace"
	decls_filename=output_filename[0]+".decls"

	#get bag info
	print "displaying bag info..."
	display_bag_info(sys.argv[1])

	#make decls file
	print "Writing decls to "+decls_filename
	decls_file=open(decls_filename, "w")
	decls_header = "input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n"
	decls_header += "\nppt ..main():::ENTER\n\tppt-type enter\n"
	decls_header += "\nppt ..main():::EXIT0\n\tppt-type subexit\n\tvariable return\n\t\tvar-kind variable\n\t\trep-type int\n\t\tdec-type int\n\t\tcomparability 1"
	decls_file.write(decls_header)
	index = 0
	for topic in topics: 
		if(testing):
			print(str(topic))
			print(type(topic))
		topic=topic[1:len(topic)]
		enter_string = "\n\nppt .."+topic+"():::ENTER\n\tppt-type enter\n"
		exit_string = "\nppt .."+topic+"():::EXIT0" + "\n\tppt-type subexit" + "\n\tvariable return" + "\n\t\tvar-kind variable" + "\n\t\trep-type hashcode" + "\n\t\tdec-type "+str(message_types[index]) + "\n\t\tcomparability 1"
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
	dtrace_file.write("input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n")
	if(testing):
		print("\nmessage_types:\n"+str(message_types))
	call_counts=np.zeros(len(topics), dtype=int)
	dtrace_file.write("\n..main():::ENTER\n")
	for topic, msg, t in bag.read_messages(topics=sys.argv[2:len(sys.argv)]):
		index = topics.index(topic)
		topic=topic.replace("/", "")
		enter_string = "\n.."+topic+"():::ENTER\nthis_invocation_nonce\n"+str(call_counts[index])+"\n"
		exit_string = "\n.."+topic+"():::EXIT0\nthis_invocation_nonce\n"+str(call_counts[index])+"\nreturn\n"+str(hex(id(msg)))+"\nreturn"+"\n"+str(hex(id(msg)))+"\n1"
		dtrace_file.write(enter_string+exit_string)
		#enumerate msg fields
		msg_type = message_types[index]
		field_string = enumerate_msg_fields(topic, msg, msg_type)
		dtrace_file.write(field_string)
		if (topic):
			call_counts[index] = call_counts[index] + 1
	dtrace_file.write("\n..main():::EXIT0\nreturn\n0\n1\n")
	dtrace_file.close()
	bag.close()
	print("--- %s seconds runtime ---" % (time.time() - start_time))



if __name__ == "__main__":
    # execute only if run as a script
    main()
