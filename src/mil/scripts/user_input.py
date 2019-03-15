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
from std_msgs.msg import Int64


obstacle_detected = False
obstacle_dyn = False
machine_state = MachineStateEnum.Default
mission_state = MissionStateEnum.Default


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


def obstacle_callback(data):
	global obstacle_detected
	obstacle_detected=data


def process_machine_state(data):
	global machine_state
	strdata = str(data)
	if("GO TO GOAL" in strdata):
		gtg=True
	else:
		gtg=False


def process_mission_state(data):
	global mission_state
	
	strdata = str(data)
	if("GO TO GOAL" in strdata):
		gtg=True
	elif:
		gtg=False


def readInputBehavior():
	timeout = 5
	print("Manual or go to goal?")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline()
	else:
		print("Unreadable; try again:")
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			s = sys.stdin.readline()
		else:
			s = "invalid"
	if("man" in s):
		print("Enable user 1 or user 2? user1 / user2")
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			s = sys.stdin.readline()
		else:
			s="invalid"
	print("Enter goal coordinates: x,y")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s += sys.stdin.readline()
	else:
		s="invalid"
	return s


def main():
	global obstacle_detected, obstacle_dyn, gtg
	rospy.init_node("user_input", anonymous=True)
	dt = 0.200
	rate = rospy.Rate(dt)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=5)
	obstacle_subscriber = rospy.Subscriber("/obstacle_detector", Bool, obstacle_callback, queue_size=1)
	user_input_publisher = rospy.Publisher("/user_input", String, queue_size=10)
	machine_state_subscriber = rospy.Subscriber("/machine_state", String, process_machine_state, queue_size=10)
	mission_state_subscriber = rospy.Subscriber("/mission_state", String, process_mission_state, queue_size=10)
	vel = Twist()
	while not rospy.is_shutdown():
		#TODO: test threading + timeout
		if(obstacle_detected and not obstacle_dyn):
			answer = readInputSelect()
		if(not gtg):
			answer = readInputBehavior()
		if("invalid" not in answer):
			user_input_publisher.publish(answer)
			sent = 0
			while(sent < 5):
				user_input_publisher.publish(answer)
				sent += 1
		else:
			print("Invalid user input; not publishing.")
		rate.sleep()


if __name__ == "__main__":
    main()
