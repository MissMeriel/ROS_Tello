#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool


def main():
	obstacle_detected = False
	rospy.init_node("obstacle_detector", anonymous=True)
	dt = 1.0/20.0
	rate = rospy.Rate(dt)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=10)
	count = 0
	while not rospy.is_shutdown():
		if(count < 10):
			obstacle_detected = False
		else:
			obstacle_detected = True
		obstacle_publisher.publish(Bool(obstacle_detected))
		rate.sleep()
		count += 1
		count = count % 20


if __name__ == "__main__":
    main()
