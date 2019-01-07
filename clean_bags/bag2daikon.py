#/usr/bin/python
import sys
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml

def display_bag_info(bag_name):
    bag_info = yaml.load(subprocess.Popen(
        ['rosbag', 'info', '--yaml', bag_name], stdout=subprocess.PIPE).communicate()[0])

    """ Get the topics in the bag """
    bag_topics = bag_info['topics']
    bag = rosbag.Bag(bag_name)

    """ For every topic in the bag, display its fields. Only do this once per topic """
    for topic in bag_topics:
        for _, msg, _ in bag.read_messages(topics=topic['topic']):
            """ Recursively list the fields in each message """
            print_topic_fields(topic['topic'], msg, 0)
            print('')
            break
    bag.close()
    sys.stdout.write("Found %u topics\n" % len(bag_topics))


def print_topic_fields(field_name, msg, depth):
    if hasattr(msg, '__slots__'):
        print(' ' * (depth * 2) + field_name)
        for slot in msg.__slots__:
            print_topic_fields(slot, getattr(msg, slot), depth + 1)
    elif isinstance(msg, list):
        if (len(msg) > 0) and hasattr(msg[0], '__slots__'):
            print(' ' * (depth * 2) + field_name + '[]')
            for slot in msg[0].__slots__:
                print_topic_fields(slot, getattr(msg[0], slot), depth + 1)
    else:
        print(' ' * (depth * 2) + field_name)
	print(' ' * (depth * 2) + "type of "+field_name+": "+str(type(msg)))

def print_return_fields(decl_file, topic):
	for _, msg, _ in bag.read_messages(topic):
		print_return_fields2(topic['topic'], msg, 0)

def print_return_fields2(field_name, msg, depth):
    if hasattr(msg, '__slots__'):
        print(' ' * (depth * 2) + field_name)
        for slot in msg.__slots__:
            print_return_fields2(slot, getattr(msg, slot), depth + 1)
    elif isinstance(msg, list):
        if (len(msg) > 0) and hasattr(msg[0], '__slots__'):
            print(' ' * (depth * 2) + field_name + '[]')
            for slot in msg[0].__slots__:
                print_return_fields2(slot, getattr(msg[0], slot), depth + 1)
    else:
        print(' ' * (depth * 2) + field_name)
	print(' ' * (depth * 2) + "type of "+field_name+": "+str(type(msg)))



bag = rosbag.Bag(sys.argv[1])
output_filename=sys.argv[1].split(".")
dtrace_filename=output_filename[0]+".dtrace"
decls_filename=output_filename[0]+".decls"

#get bag info
info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', sys.argv[1]], stdout=subprocess.PIPE).communicate()[0])
#print info_dict
#topics = bag.get_type_and_topic_info()[1].keys()
#print "topics via bag call: "+str(topics)
print "displaying bag info.."
display_bag_info(sys.argv[1])

#make decls file
print "Writing decls to "+decls_filename
topic_set = Set()
#fields_dicts = {}
msg_count = 0
for topic, msg, t in bag.read_messages(topics=sys.argv[2:len(sys.argv)]):
	topic_set.add(topic)
	if (msg):
		msg_count +=1
		#fields = []
		#msg = msg.split('\n')
		#for string in msg:
		#	string = string.split(":")[0]
	#print topic
	#print type(msg)
decls_file=open(decls_filename, "w")
decls_file.write("input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n")
print "message count: "+str(msg_count)
decls_file.write("\nppt ..main():::ENTER\n\tppt-type enter\n")
decls_file.write("\nppt ..main():::EXIT0\n\tppt-type subexit\n\tvariable return\n\t\tvar-kind variable\n\t\trep-type int\n\t\tdec-type int\n\t\tcomparability 1\n")
for topic in topic_set:
	topic=topic.replace("/", "")
	decls_file.write("\nppt .."+topic+"():::ENTER\n\tppt-type enter\n")
	decls_file.write("\nppt .."+topic+"():::EXIT0\n\tppt-type subexit\n")
decls_file.close()

#make dtrace file
print "Writing dtrace to "+dtrace_filename
dtrace_file=open(dtrace_filename, "w")
dtrace_file.write("input-language C/C++\ndecl-version 2.0\nvar-comparability implicit\n\n")
topic_list=list(topic_set)
call_counts=np.zeros(len(topic_set), dtype=int)
dtrace_file.write("\n..main():::ENTER\n")
#dtrace_file.write("\n..main():::ENTER\nthis_invocation_nonce\n0\n")
for topic, msg, t in bag.read_messages(topics=sys.argv[2:len(sys.argv)]):
	index = topic_list.index(topic)
	topic=topic.replace("/", "")
	dtrace_file.write("\n.."+topic+"():::ENTER")
	dtrace_file.write("\nthis_invocation_nonce")
	dtrace_file.write("\n"+str(call_counts[index]))
	dtrace_file.write("\n")
	dtrace_file.write("\n.."+topic+"():::EXIT0")
	dtrace_file.write("\nthis_invocation_nonce")
	dtrace_file.write("\n"+str(call_counts[index]))
	dtrace_file.write("\n")
	#dtrace_file.write("")
	if (topic):
		call_counts[index] = call_counts[index] + 1
print "call counts"
index=0
for topic in topic_list:
	print "\t"+str(topic_list[index])+": "+call_counts[index]
	index += 1
dtrace_file.write("\n..main():::EXIT0\nreturn\n0\n1\n")
#dtrace_file.write("\n..main():::EXIT0\nthis_invocation_nonce\n0\nreturn\n0\n1\n")
dtrace_file.close()
bag.close()
