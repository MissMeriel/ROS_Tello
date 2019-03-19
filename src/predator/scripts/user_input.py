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

from PredatorEnum import MachineState, MissionState, UserState
#from MissionStateEnum import MissionState

obstacle_detected = False
obstacle_dyn = False
machine_state = MachineState.Default
mission_state = MissionState.Default


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


def obstacle_callback(msg):
	global obstacle_detected
	obstacle_detected=msg


def process_machine_state(msg):
	global machine_state
	strdata = str(msg.data)
	if(strdata == str(MachineState.Hovering)):
		machine_state = MachineState.Hovering
	elif(strdata == str(MachineState.Sweeping)):
		machine_state = MachineState.Sweeping
	elif(strdata == str(MachineState.GoToGoal)):
		machine_state = MachineState.GoToGoal
	elif(strdata == str(MachineState.NoVicon)):
		machine_state = MachineState.NoVicon
	else:
		machine_state=MachineState.Default
	print("machine_state = "+strdata)


def process_mission_state(msg):
	global mission_state
	strdata = str(msg.data)
	if(strdata == str(MissionState.Complete)):
		mission_state = MissionState.Complete
	elif(strdata == str(MissionState.InProgress)):
		mission_state = MissionState.InProgress
	elif(strdata == str(MissionState.WaitingForUser)):
		mission_state = MissionState.WaitingForUser
	else:
		mission_state = MissionState.Default
	print("mission_state = "+strdata)

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
	global obstacle_detected, obstacle_dyn, machine_state, mission_state
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
		answer = "answer"
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
