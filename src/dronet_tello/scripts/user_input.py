#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
#import msvcrt #only on Windows
#import signal #only on Lnux
from select import select
from threading import Thread

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool

obstacle_detected = False

def obstacle_callback(data):
	global obstacle_detected
	obstacle_detected = data


def readInput( caption, default, timeout = 5):
	start_time = time.time()
	sys.stdout.write('%s(%s):'%(caption, default));
	input = ''
	while True:
		if msvcrt.kbhit():
			chr = msvcrt.getche()
			if ord(chr) == 13: # enter_key
				break
			elif ord(chr) >= 32: #space_char
				input += chr
		if len(input) == 0 and (time.time() - start_time) > timeout:
			break

	print ''  # needed to move to next line
	if len(input) > 0:
		return input
	else:
		return default


def readInputSelect():
	timeout = 5
	print("Avoid obstacle?")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline()
	else:
		s = "no"
	return s


def main():
	global obstacle_detected
	rospy.init_node("user_input", anonymous=True)
	dt = 0.200
	rate = rospy.Rate(dt)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=5)
	obstacle_subscriber = rospy.Subscriber("/obstacle_detector", Bool, obstacle_callback, queue_size=1)
	user_input_publisher = rospy.Publisher("/user_input", String, queue_size=10)
	vel = Twist()
	while not rospy.is_shutdown():
		if(obstacle_detected):
			vel.linear.x = 0
			vel.linear.y = 0
			sent = 0
			while(sent < 5):
				velocity_publisher.publish(vel)
				sent += 1
			#user input
			#TODO: test threading + timeout
			answer = readInputSelect()

			sent = 0
			while(sent < 5):
				user_input_publisher.publish(answer)
				sent += 1

		rate.sleep()


if __name__ == "__main__":
    main()
