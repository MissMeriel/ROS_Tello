#/usr/bin/python
import rosbag
import sys

bag = rosbag.Bag(sys.argv[1])
for topic, msg, t in bag.read_messages(topics=sys.argv[2:len(sys.argv)]):
	print topic
#	print t
#	print msg
bag.close()
