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

from PredatorEnum import MachineState, MissionState, UserState, UserCommand, WarningState

obstacle_detected = False
obstacle_dyn = False
machine_state = MachineState.Default
mission_state = MissionState.Default


#For reading input on Windows
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
	#elif(strdata == str(MachineState.GoToGoal)):
	#	machine_state = MachineState.GoToGoal
	elif(strdata == str(MachineState.NoVicon)):
		machine_state = MachineState.NoVicon
	elif(strdata == str(MachineState.PossibleTargetDetected)):
		machine_state = MachineState.PossibleTargetDetected
	else:
		machine_state=MachineState.Default
	#print("machine_state = "+strdata)


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


def process_warning_state(msg):
	global warning_state
	strdata = str(msg.data)
	if(strdata == str(WarningState.NoVicon)):
		error_state = WarningState.NoVicon
	if(strdata == str(WarningState.LosingVicon)):
		error_state = WarningState.LosingVicon
	if(strdata == str(WarningState.LowBattery)):
		error_state = WarningState.LowBattery
	print("warning_state: "+str(strdata))


def readInputEmergencyLand():
	timeout = 5
	s = ""
	enum = UserCommand.Default
	print("Emergency land? y/n")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline()
	else:
		s = "no"
	return s


def readInputPossibleTargetDetected():
	enum = UserCommand.Default
	print("Possible target detected. Options are:\n\tLook closer: 1\n\tAdd 5 seconds to hover: 2\n\tTarget is correct, return home: 3\n\tTarget is incorrect, keep sweeping: 4\nInput your response: ")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline().lower()
	else:
		print("Unreadable; try again:")
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			s = sys.stdin.readline()
		else:
			s = "invalid"
	try:
		choice = int(s)
		if(choice == 1):
			enum = UserCommand.LookCloser
		elif(choice == 2):
			enum = UserCommand.Hover
		elif(choice == 3):
			enum = UserCommand.ReturnHome
		elif(choice == 4):
			enum = UserCommand.KeepSweeping
		#else:
		#	enum = UserCommand.Land
	except:
		enum = UserCommand.Land
	return enum

def readInputFinishedBehavior()
	enum = UserCommand.Default
	print("Finished behavior. Options are:\n\tReturn to base: 1\n\tSweep again: 2\nInput your response:")
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline().lower()
	else:
		print("Unreadable; try again:")
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			s = sys.stdin.readline()
		else:
			s = "invalid"
	try:
		choice = int(s)
		if(choice == 1):
			enum = UserCommand.ReturnHome
		elif(choice == 2):
			enum = UserCommand.SweepAgain
		else:
			enum = UserCommand.Land
	except:
		enum = UserCommand.Land


def readInputBehavior():
	global obstacle_detected, obstacle_dyn, machine_state, mission_state, warning_state
	timeout = 5
	s = ""
	enum = UserCommand.Default
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline().lower()
	if('land' in s):
		return UserCommand.Land
	if('auto' in s):
		return UserCommand.RequestAutoControl
	if(machine_state == MachineState.PossibleTargetDetected):
		enum = readInputPossibleTargetDetected()
	elif(machine_state == MachineState.FinishedBehavior):
		enum = readInputFinishedBehavior
	elif(machine_state == MachineState.NoVicon or warning_state == WarningState.NoVicon):
		enum = readInpuyNoVicon
	return enum


def main():
	global obstacle_detected, obstacle_dyn, machine_state, mission_state, warning_state
	rospy.init_node("user_input", anonymous=True)
	dt = 0.200
	rate = rospy.Rate(dt)
	user_input_publisher = rospy.Publisher("/user_input", String, queue_size=10)
	machine_state_subscriber = rospy.Subscriber("/machine_state", String, process_machine_state, queue_size=2)
	mission_state_subscriber = rospy.Subscriber("/mission_state", String, process_mission_state, queue_size=2)
	error_state_subscriber = rospy.Subscriber("/error_state", String, process_error_state, queue_size=2)
	vel = Twist()
	print("To request emergency land at any time, input \"land\".")
	while not rospy.is_shutdown():
		#TODO: test threading + timeout
		answer = str(readInputBehavior())
		if("invalid" not in answer and "Default" not in answer):
			print(answer)
			user_input_publisher.publish(answer)
			sent = 1
			while(sent < 1):
				user_input_publisher.publish(answer)
				sent += 1
		#else:
		#	print("Invalid user input; not publishing.")
		rate.sleep()


if __name__ == "__main__":
    main()
