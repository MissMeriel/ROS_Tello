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
import std_msgs.msg
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int64
from dronet_tello.msg import HeadedString
from PredatorEnum import MachineState, MissionState, UserState, UserCommand, WarningState, CommandState

obstacle_detected = False
obstacle_dyn = False
machine_state = MachineState.Default
mission_state = MissionState.Default
user_cmd = UserCommand.Default
warning_state = WarningState.Default
timeout = 7
vicon_restored = False

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
	elif(strdata == str(MachineState.OutsideSweepArea)):
		machine_state = MachineState.OutsideSweepArea
	elif(strdata == str(MachineState.LosingVicon)):
		machine_state = MachineState.LosingVicon
	elif(strdata == str(MachineState.NoVicon)):
		machine_state = MachineState.NoVicon
	elif(strdata == str(MachineState.PossibleTargetDetected)):
		machine_state = MachineState.PossibleTargetDetected
	elif(strdata == str(MachineState.FinishedBehavior)):
		machine_state = MachineState.FinishedBehavior
	elif(strdata == str(MachineState.Landing)):
		machine_state = MachineState.Landing
	elif(strdata == str(MachineState.Manual)):
		machine_state = MachineState.Manual
	elif(strdata == str(MachineState.TransferringControl)):
		machine_state = MachineState.TransferringControl
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
	#print("mission_state: "+strdata)


def process_warning_state(msg):
	global warning_state, vicon_restored
	vicon_restored = False
	strdata = str(msg.data)
	if("Vicon" in str(warning_state) and strdata == str(WarningState.Default)):
		vicon_restored = True
	if(strdata == str(WarningState.NoVicon)):
		warning_state = WarningState.NoVicon
	elif(strdata == str(WarningState.LosingVicon)):
		warning_state = WarningState.LosingVicon
	elif(strdata == str(WarningState.LowBattery)):
		warning_state = WarningState.LowBattery
	elif(strdata == str(WarningState.Default)):
		warning_state = WarningState.Default
	#print("warning_state: "+str(strdata))


def process_command_state(msg):
	global command_state
	strdata = str(msg.data)
	if(strdata == str(CommandState.Auto)):
		command_state = CommandState.Auto
	if(strdata == str(CommandState.Manual)):
		command_state = CommandState.Manual


def readInputEmergencyLand():
	global timeout
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
	global timeout
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
			enum = UserCommand.KeepHovering
		elif(choice == 3):
			enum = UserCommand.ReturnHome
		elif(choice == 4):
			enum = UserCommand.KeepSweeping
		#else:
		#	enum = UserCommand.Land
	except:
		print("Exception on parsing input")
		enum = UserCommand.Land
	return enum


def readInputFinishedBehavior():
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
	return enum


def readInputNoVicon():
	#global 
	enum = UserCommand.Default
	print("Losing vicon connection. Options are:\n\tManual control: 1\n\tAuto control: 2\n\tEmergency land: 3\nInput your response:")
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
			enum = UserCommand.RequestManualControl
		elif(choice == 2):
			enum = UserCommand.RequestAutoControl
		else:
			enum = UserCommand.Land
	except:
		enum = UserCommand.Land
	return enum


def readInputRequestAutoControl():
	#global 
	enum = UserCommand.Default
	if(machine_state != MachineState.NoVicon):
		print("Request for auto control. Options are:\n\tSwitch to manual mode: 1\n\tStay in auto control: 2\n\tEmergency land: 3\nInput your response:")
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
	else:
		print("No Vicon connectivity -- cannot return to autonomous control.")
		print("Still in manual mode.")
		enum = UserCommand.Default
	return enum


def readInputBehavior():
	global machine_state, mission_state, warning_state, user_cmd, vicon_restored
	timeout = 5
	s = ""
	enum = UserCommand.Default
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		s = sys.stdin.readline().lower()
	if('land' in s):
		enum = UserCommand.Land
	elif('auto' in s):
		enum = UserCommand.RequestAutoControl
		#return UserCommand.RequestAutoControl
	elif("Vicon" in str(warning_state) and user_cmd != UserCommand.RequestManualControl):
		print("machine_state:"+str(machine_state)+"\nmission_state: "+str(mission_state)+"\nwarning_state: "+str(warning_state)+"\nuser_cmd: "+str(user_cmd))
		enum = readInputNoVicon()
	elif(machine_state == MachineState.PossibleTargetDetected):
		enum = readInputPossibleTargetDetected()
	elif(machine_state == MachineState.FinishedBehavior):
		enum = readInputFinishedBehavior()
	elif(user_cmd == UserCommand.RequestAutoControl and machine_state == MachineState.Manual):
		enum = readInputRequestAutoControl()
	user_cmd = enum
	return enum


def main():
	global obstacle_detected, obstacle_dyn, machine_state, mission_state, warning_state
	rospy.init_node("user_input", anonymous=True)
	dt = 0.200
	rate = rospy.Rate(dt)
	user_input_publisher = rospy.Publisher("/user_input", HeadedString, queue_size=10)
	machine_state_subscriber = rospy.Subscriber("/machine_state", HeadedString, process_machine_state, queue_size=1)
	mission_state_subscriber = rospy.Subscriber("/mission_state", HeadedString, process_mission_state, queue_size=1)
	warning_state_subscriber = rospy.Subscriber("/warning_state", HeadedString, process_warning_state, queue_size=2)
	vel = Twist()
	command_state_subscriber = rospy.Subscriber("/command_state", HeadedString, process_command_state, queue_size=2)
	print("To request emergency land at any time, input \"land\".")
	print("To request auto control at any time, input \"auto\".")
	while not rospy.is_shutdown():
		#TODO: test threading + timeout
		#print("machine_state:"+str(machine_state)+"\nmission_state: "+str(mission_state)+"\nwarning_state: "+str(warning_state)+"\nuser_cmd: "+str(user_cmd)) 
		answer = str(readInputBehavior())
		if("invalid" not in answer and "Default" not in answer):
			print(answer)
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = answer
			user_input_publisher.publish(headed_str_msg)
			sent = 1
			#while(sent < 1):
			#	user_input_publisher.publish(headed_str_msg)
			#	sent += 1
		#else:
		#	print("Invalid user input; not publishing.")
		rate.sleep()


if __name__ == "__main__":
    main()
