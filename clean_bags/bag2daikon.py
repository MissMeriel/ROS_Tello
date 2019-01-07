#/usr/bin/python
import sys
import rosbag
from sets import Set
import numpy as np

bag = rosbag.Bag(sys.argv[1])
output_filename=sys.argv[1].split(".")
dtrace_filename=output_filename[0]+".dtrace"
decls_filename=output_filename[0]+".decls"

#make decls file
print "Writing decls to "+decls_filename
topic_set = Set()
msg_count = 0
for topic, msg, t in bag.read_messages(topics=sys.argv[2:len(sys.argv)]):
	topic_set.add(topic)
	if (msg):
		msg_count +=1
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
