#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
import numpy as np
import std_msgs.msg
from std_msgs.msg import String
from std_msgs.msg import Int8
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import PoseStamped
from dronet_tello.msg import FlightData
from dronet_tello.msg import HeadedBool 
from dronet_tello.msg import HeadedString
import rosgraph.impl.graph as rig
from PredatorEnum import MachineState, MissionState, UserState, UserCommand, WarningState, CommandState

#take in form of x1,x2,x3,x4...
goal_x = sys.argv[1]
goal_y = sys.argv[2]
goal_z = sys.argv[3]
interpolation_x = []
interpolation_y = []
interpolation_z = []
curr_x = 0
curr_y = 0
curr_z = 0
curr_angle = 0
home_x = -200
home_y = -200
threshold = 0.1
publishing = True
kill = False
sweeping = False
possible_target_detected = False
old_height = 0
battery_percentage = 100
battery_low = False
user_input = str(UserCommand.Default)
ignore_map = {'x':[], 'y':[], 'z':[]}
baseline_hover_threshold = 10
hover_threshold = baseline_hover_threshold
ignore = False
machine_state = MachineState.Default
command_state = CommandState.Default
mission_state = MissionState.Default
warning_state = WarningState.Default

def process_sysargs():
	global goal_x, goal_y, goal_z, interpolation_x, interpolation_y, interpolation_z, curr_x, curr_y, curr_z
	goal_x = goal_x.split(",")
	goal_y = goal_y.split(",")
	goal_z = goal_z.split(",")
	for i in range(0,len(goal_x)):
		goal_x[i] = float(goal_x[i])
		goal_y[i] = float(goal_y[i])
		goal_z[i] = float(goal_z[i])
	# pick closer goal, make first entry in interpolations
	distance_1 = math.sqrt((curr_x-goal_x[0])**2+(curr_y-goal_y[0])**2+(curr_z-goal_z[0])**2)
	distance_2 = math.sqrt((curr_x-goal_x[1])**2+(curr_y-goal_y[1])**2+(curr_z-goal_z[1])**2)
	if(distance_1 < distance_2):
		print(goal_x[0])
		print(len(interpolation_x))
		interpolation_x.append(goal_x[0])
		interpolation_y.append(goal_y[0])
		interpolation_z.append(goal_z[0])
	else:
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[1])
		interpolation_z.append(goal_z[1])
		goal_x[1] = goal_x[0]
		goal_y[1] = goal_y[0]
		goal_z[1] = goal_z[0]
		goal_x[0] = interpolation_x[0]
		goal_y[0] = interpolation_y[0]
		goal_z[0] = interpolation_z[0]
	interpolate(0.1)


# Traverses between xy coordinates starting at nearest point
def interpolate(increment_z):
	global goal_x, goal_y, goal_z, interpolation_x, interpolation_y, interpolation_z
	index = 2
	for i in frange(goal_z[0], goal_z[1], increment_z):
		interpolation_z.append(i)
		if(index % 2 == 0 or i == goal_x[1]):
			interpolation_x.append(goal_x[1])
			interpolation_y.append(goal_y[1])
		else:
			interpolation_x.append(goal_x[0])
			interpolation_y.append(goal_y[0])
		index += 1
	if(interpolation_x[len(interpolation_x)-1] != goal_x[1]):
		# need one more traverse
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[1])
		interpolation_z.append(goal_z[1])


def frange(start, stop, step):
	i = start
	if(stop < start):
		step = -step
		while i > stop:
			yield round(i,2)
			i = float(i + step)
	else:
		while i < stop:
			yield round(i,2)
			i = float(i + step)


def vicon_data(msg):
	global curr_x, curr_y, curr_z, curr_angle
	global home_x, home_y
	global publishing
	curr_x = msg.transform.translation.x
	curr_y = msg.transform.translation.y
	curr_z = msg.transform.translation.z
	# quaternions to radians
	siny_cosp = +2.0 * (msg.transform.rotation.w * msg.transform.rotation.z + msg.transform.rotation.x * msg.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (msg.transform.rotation.y * msg.transform.rotation.y + msg.transform.rotation.z * msg.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True
	if(curr_z < 0.05):
		home_x = msg.transform.translation.x
		home_y = msg.transform.translation.y


def process_flight_data(msg):
	global sweeping, battery_percentage, battery_low, warning_state
	# height == VPS data
	battery_percentage = msg.battery_percentage
	battery_low = bool(msg.battery_low)
	if(battery_low == True):
		warning_state = WarningState.LowBattery

def process_visp_auto_tracker_status(msg):
	global possible_target_detected, ignore, machine_state, command_state
	#if (data.data >= 3 and not ignore):
	if(command_state != CommandState.Manual or machine_state != MachineState.Manual):
		if (msg.data == 3 or msg.data == 5 and not ignore):
			possible_target_detected = True


def process_user_input(msg):
	global user_input, hover_threshold, kill, machine_state, command_state, warning_state, mission_state
	user_input = str(msg.data)
	if("Land" in user_input):
		kill=True
	elif("KeepHovering" in user_input):
		hover_threshold += 5
	elif("Manual" in user_input):
		print("Machine in manual mode.")
		machine_state = MachineState.Manual
		command_state = CommandState.Manual
	elif("Auto" in user_input):
		if(warning_state == WarningState.NoVicon):
			print("No Vicon connectivity: cannot assume autonomous control")
			machine_state = MachineState.Manual
			command_state = CommandState.Manual
		else:
			machine_state = MachineState.Default
			command_state = CommandState.Auto
			warning_state = WarningState.Default


def process_visp_position(msg):
	global target_position_x, target_position_y, target_position_z, target_position_angle
	global curr_x, curr_y, curr_z
	target_position_x = msg.pose.position.x
	target_position_y = msg.pose.position.y
	target_position_z = msg.pose.position.z
	# quaternions to radians
	siny_cosp = +2.0 * (msg.pose.orientation.w * msg.pose.orientation.z + msg.pose.orientation.x * msg.pose.orientation.y);
	cosy_cosp = +1.0 - 2.0 * (msg.pose.orientation.y * msg.pose.orientation.y + msg.pose.orientation.z * msg.pose.orientation.z);  
	target_position_angle = math.atan2(siny_cosp, cosy_cosp);


def percent_mission_completed(goal_counter):
	global goal_x, goal_y, interpolation_x, interpolation_y, interpolation_z
	total_distance = 0.0
	for i in range(0, len(interpolation_x)):
		total_distance += math.sqrt((interpolation_x[i] - curr_x)**2 + (interpolation_y[i] - curr_y)**2 + (interpolation_z[i] - curr_z)**2)
	travelled_distance = 0.0
	for i in range(0, goal_counter+1):
		travelled_distance += math.sqrt((interpolation_x[i] - curr_x)**2 + (interpolation_y[i] - curr_y)**2 + (interpolation_z[i] - curr_z)**2)
	return "{0:.0%}".format(travelled_distance/total_distance)


def sliding_window(arr, elem):
	new_arr = arr[1:len(arr)]
	new_arr = np.append(new_arr, elem)
	return new_arr


def main():
	global goal_x, goal_y, interpolation_x, interpolation_y, interpolation_z, home_x, home_y
	global threshold, hover_threshold
	global curr_x, curr_y, curr_z, curr_angle
	global publishing, kill, sweeping, possible_target_detected
	global user_input, ignore_map, ignore
	global machine_state, command_state, mission_state, warning_state
	global target_position_x, target_position_y, target_position_z, target_position_angle

	process_sysargs()

	rospy.init_node("sweep", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=1)
	machine_state_publisher = rospy.Publisher("/machine_state", HeadedString, queue_size=1)
	mission_state_publisher = rospy.Publisher("/mission_state", HeadedString, queue_size=1)
	warning_state_publisher = rospy.Publisher("/warning_state", HeadedString, queue_size=1)
	command_state_publisher = rospy.Publisher("/command_state", HeadedString, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", HeadedString, process_user_input, queue_size=1)
	flight_data_subscriber = rospy.Subscriber("/flight_data", FlightData, process_flight_data, queue_size=5)
	visp_auto_tracker_status_subscriber = rospy.Subscriber("/visp_auto_tracker/status", Int8, process_visp_auto_tracker_status, queue_size=5)
	user_input_subscriber = rospy.Subscriber("/user_input", HeadedString, process_user_input, queue_size=1)
	visp_position_subscriber = rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, process_visp_position, queue_size=1)

	#nodemap_file = open(os.path.basename(__file__), "w")
	#nodemap_file.write(rig.topic_node('/velocity'))

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	z_integral = 0
	z_previous_error = 0
	ang_previous_error = 0
	ang_integral = 0
	sweep_threshold = 0.25

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode: Kp = 0.03; Ki = 0.003; Kd = 0.006
	Kp = 0.27 # 0.41 not good for goal near wall -- overshoot 0.41
	Ki = 0.00075
	Kd = 0.01
	Kp_fast = 0.41; Ki_fast = 0.003; Kd_fast = 0.01
	Kp_reg = 0.41; Ki_reg = 0.003; Kd_reg = 0.01;
#	Kp_slow = 0.07; Ki_slow = 0.003; Kd_slow = 0.006;
#	Kp_slow = 0.0025; Ki_slow = 0.003; Kd_slow = 0.001; #suuuuuuper slow
	Kp_slow = 0.2; Ki_slow = 0.003; Kd_slow = 0.0075;
	publishing_count = 0
	hover_count = 0
	goal_counter = 0
	home_not_set = True
	# ignore_threshold:	0.65 for QR codes of approx. 18cm width (standard letter paper)
	#			??? for QR codes of approx. (10x17" A4 paper)
	ignore_threshold = 0.065 # 0.1
	angle_facing_sweep_area = math.atan2(goal_y[0]-goal_y[1], goal_x[0]-goal_x[1]) + math.pi/2.0
	machine_state = MachineState.Default
	ignore = False
	publishing_record = np.ones(50, dtype=bool)
	look_closer_count = 0
	exit_count = 0
	backup_count = 0
	if("Vicon" in str(warning_state)):
		warning_state = str(WarningState.Default)
	mission_state = MissionState.Default

	while not rospy.is_shutdown():

		#3D Euclidean distance
		distance_to_goal = math.sqrt((interpolation_x[goal_counter] - curr_x)**2 + (interpolation_y[goal_counter] - curr_y)**2)
		z_distance_to_goal = interpolation_z[goal_counter] - curr_z
		if(home_x != -200 and home_not_set):
			interpolation_x.append(home_x)
			interpolation_y.append(home_y)
			interpolation_z.append(0)
			home_not_set = False
		print("")
		percent_mission = percent_mission_completed(goal_counter)
		print("ignore: "+str(ignore))
		print("kill: "+str(kill))
		print("% mission completed: "+ percent_mission)
		print("waypoints visited: "+str(goal_counter)+"/"+str(len(interpolation_x)-1))
		print("interpolation_x: "+str(interpolation_x))
		print("interpolation_y: "+str(interpolation_y))
		print("interpolation_z: "+str(interpolation_z))
		print("home: "+str(home_x)+","+str(home_y))
		print("curr_x, curr_y, curr_z: "+str(curr_x)+", "+str(curr_y)+", "+str(curr_z))
		print("curr_angle: "+str(math.degrees(curr_angle)))
		#print("goal_x: "+str(goal_x))
		#print("goal_y: "+str(goal_y))
		#print(""+str(math.degrees(angle_facing_sweep_area)))
		angle_to_goal = math.atan2(interpolation_y[goal_counter]-curr_y, interpolation_x[goal_counter]-curr_x) - curr_angle
		raw_angle_to_goal = math.atan2(interpolation_y[goal_counter]-curr_y, interpolation_x[goal_counter]-curr_x)
		desired_angle = math.atan2(goal_y[1]-goal_y[0], goal_x[1]-goal_x[0]) + math.radians(90)

		# Returned to base or user-requested land
		if(kill):
			# send land cmd then exit
			if("Land" in user_input):
				strmsg = "User requested land"
				mission_state = MissionState.Abort
				warning_state = WarningState.AbortingMission
			else:
				strmsg = "Returned to base; landing"
				mission_state = MissionState.Complete
				#warning_state = WarningState.Default
			machine_state = MachineState.Landing
			print(strmsg)
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			velocity_publisher.publish(vel)
			velocity_publisher.publish(vel)
			velocity_publisher.publish(vel)
			velocity_publisher.publish(vel)
			velocity_publisher.publish(vel)
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = str(machine_state)
			machine_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(mission_state)
			mission_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(warning_state)
			mission_state_publisher.publish(headed_str_msg)
			exit_count+= 1
			if(exit_count > 5):
				exit()
			continue

		# in manual control mode
		if(machine_state == str(MachineState.Manual) and str(command_state) == CommandState.Auto and not kill):
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = str(machine_state)
			machine_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(MissionState.InProgress)
			mission_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(CommandState.Manual)
			command_state_publisher.publish(headed_str_msg)
			continue
		else:
			command_state = CommandState.Auto
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = str(command_state)
			command_state_publisher.publish(headed_str_msg)

		# Check if current spot has been seen & adjudicated
		for i in range(0,len(ignore_map['x'])):
			if math.sqrt((curr_x - ignore_map['x'][i])**2+(curr_y - ignore_map['y'][i])**2+(curr_z - ignore_map['z'][i])**2) < ignore_threshold:
				ignore = True
			else:
				ignore = False

		# check for lapse in vicon data
		publishing_record = sliding_window(publishing_record, publishing)
		print("publishingrecord over 1/2 false: "+str(publishing_record.tolist().count(False) > len(publishing_record)/3.0))
		if(not publishing and machine_state != MachineState.Manual):
			publishing_count += 1
		else:
			publishing_count = 0
		if(publishing_count > 5 and machine_state != MachineState.Manual and machine_state != MachineState.Hovering):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = 0
			warning_state = str(WarningState.NoVicon)
			machine_state = str(MachineState.Hovering)
			print(str(WarningState.NoVicon))
			print(str(MachineState.Hovering))
			print(str(mission_state))
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = str(MachineState.Hovering)
			machine_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(WarningState.NoVicon)
			warning_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(mission_state)
			machine_state_publisher.publish(headed_str_msg)
			velocity_publisher.publish(vel)
			continue
		elif(publishing_record.tolist().count(False) > len(publishing_record)/2.0 and machine_state != MachineState.Manual):
			warning_state = str(WarningState.LosingVicon)
			machine_state = str(MachineState.LosingVicon)
			#print(machine_state)
			#print(str(WarningState.LosingVicon))
			h = std_msgs.msg.Header()
			h.stamp = rospy.Time.now()
			headed_str_msg = HeadedString()
			headed_str_msg.header = h
			headed_str_msg.data = machine_state
			machine_state_publisher.publish(headed_str_msg)
			headed_str_msg.data = str(warning_state)
			warning_state_publisher.publish(headed_str_msg)
			#if("Default" in user_input):
			#	mission_state = MissionState.WaitingForUser
			#	headed_str_msg.data = str(mission_state)
			#	mission_state_publisher.publish(headed_str_msg)

		#Finished sweep
		elif (distance_to_goal < sweep_threshold and z_distance_to_goal < sweep_threshold and interpolation_x[goal_counter] == goal_x[1] and interpolation_x[goal_counter] == goal_y[1] and interpolation_z[goal_counter] == goal_z[1] and machine_state != MachineState.Manual):
			vel.linear.x = 0
			vel.linear.y = 0
			hover_count += dt
			#query user for options: Sweep again? Inspect specific point? Go home?
			strmsg = str(MachineState.FinishedBehavior)
			machine_state = MachineState.FinishedBehavior
			mission_state = MissionState.FinishedBehavior
			if(hover_count > 10 and goal_counter < len(goal_x)-1):
				hover_count = 0
				integral = 0
				previous_error = 0
				ang_previous_error = 0
				ang_integral = 0
				goal_counter +=1
			#print(strmsg)
			#velocity_publisher.publish(vel)
			#machine_state_publisher.publish(str(machine_state))
			#mission_state_publisher.publish(str(mission_state))
			Kp = Kp_reg; Ki = Ki_reg; Kd = Kd_reg

		#arrived back to home base
		elif(distance_to_goal < sweep_threshold and z_distance_to_goal < sweep_threshold and abs(interpolation_x[goal_counter] - home_x) < sweep_threshold and abs(interpolation_y[goal_counter] - home_y) < sweep_threshold and machine_state != MachineState.Manual):
			vel.linear.x = 0
			vel.linear.y = 0
			if(hover_count > 2):
				vel.linear.z = -200
				velocity_publisher.publish(vel)
				strmsg = "Returned to home base"
				machine_state = MachineState.Landing
				mission_state = MissionState.Complete
				#machine_state_publisher.publish(str(machine_state))
			elif(hover_count > 2 and goal_counter == len(goal_x)-1):
				exit()
			#print(strmsg)
			#print(machine_state)
			#print(mission_state)
			#velocity_publisher.publish(vel)
			#machine_state_publisher.publish(strmsg)
			hover_count += dt
			
		#reached sweeping area
		elif (distance_to_goal < sweep_threshold and goal_counter == 0 and machine_state != MachineState.Manual):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = 0
			strmsg = "SWEEP AREA REACHED"
			machine_state = MachineState.Sweeping
			if(hover_count > 5 and goal_counter == 0):
				goal_counter += 1
				hover_count = 0
			#print(strmsg)
			#velocity_publisher.publish(vel)
			#machine_state_publisher.publish(str(machine_state))
			hover_count += dt
			integral = 0
			previous_error = 0
			z_integral = 0
			z_previous_error = 0
			ang_previous_error = 0
			ang_integral = 0
			Kp = Kp_slow; Ki = Ki_slow; Kd = Kd_slow;

		#reached an interpolated goal
		elif (distance_to_goal < sweep_threshold and z_distance_to_goal < sweep_threshold and "LookCloser" not in user_input):  # and machine_state != MachineState.Manual):
			if(hover_count < 1 and goal_counter < len(interpolation_x)-1):
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = 0
				strmsg = "SWEEPING; REACHED INTERPOLATION POINT"
			#elif(hover_count >= 1 and goal_counter < len(interpolation_x)-1):
			else:
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = 0
				strmsg = "SWEEPING; LEAVING INTERPOLATION POINT"
				hover_count = 0
				integral = 0
				previous_error = 0
				z_integral = 0
				z_previous_error = 0
				ang_previous_error = 0
				ang_integral = 0
				goal_counter += 1
			#print(strmsg)
			machine_state = MachineState.Sweeping
			mission_state = MissionState.InsideSweepArea
			hover_count += dt
			#velocity_publisher.publish(vel)
			#machine_state_publisher.publish(str(machine_state))
			#mission_state_publisher.publish(str(mission_state))

		elif(machine_state != MachineState.Manual):
			if(possible_target_detected and goal_counter < len(interpolation_x)-1 and goal_counter > 0 and not ignore):
				#query user for options: Sweep again? Inspect specific point? Go home?
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = 0
				previous_error = 0
				integral = 0
				z_previous_error = 0
				z_integral = 0
				hover_count += dt
				if("LookCloser" not in user_input):
					machine_state = MachineState.PossibleTargetDetected
					mission_state = MissionState.PossibleTargetDetected
					strmsg = str(MachineState.PossibleTargetDetected)
				#print("hover_count: "+str(hover_count))
				# look closer auto
				if("LookCloser" in user_input):
					if(look_closer_count < 2.25):
						hover_count = 0
						vel.linear.x = 0.15
						vel.linear.y = 0 
						look_closer_count += dt
					elif(hover_count < 5):
						vel.linear.x = 0
						vel.linear.y = 0
					else:
						vel.linear.x = -0.15
						vel.linear.y = 0
						hover_count = 0
						look_closer_count = 0
				#elif("RequestAutoControl" in user_input and "Vicon" in str(warning_state)):
				#	if(backup_count < 3):
				#		vel.linear.x = -0.15
				#		vel.linear.y = 0
				#		backup_count += dt
				#	else:
				#		hover_count = 0
				#		look_closer_count = 0
				#		backup_count = 0
				elif(hover_count > hover_threshold or "KeepSweeping" in user_input):
					#goal_counter = len(interpolation_x)-1
					#possible_target_detected = False
					ignore = True
					ignore_map['x'].append(curr_x)
					ignore_map['y'].append(curr_y)
					ignore_map['z'].append(curr_z)
				elif('ReturnHome' in user_input):
					hover_count = 0
					hover_threshold = baseline_hover_threshold
					goal_counter = len(interpolation_x)-1
				else:
					hover_count = 0
					hover_threshold = baseline_hover_threshold
					possible_target_detected = False
			else:
				if(goal_counter == 0):
					strmsg = "APPROACHING SWEEP AREA"
				elif(goal_counter == len(interpolation_x)-1):
					strmsg = "LEAVING SWEEP AREA"
					Kp = Kp_reg; Ki = Ki_reg; Kd = Kd_reg;
					mission_state = MissionState.OutsideSweepArea
					machine_state = MachineState.FinishedBehavior
				else:
					strmsg = "SWEEPING"
					Kp = Kp_slow; Ki = Ki_slow; Kd = Kd_slow;
					machine_state = MachineState.Sweeping
					mission_state = MissionState.InsideSweepArea
				error = distance_to_goal
				derivative = (error - previous_error) / dt
				integral = integral + (error * dt)
				w = Kp*error + Ki*integral + Kd*derivative
				previous_error = error

				z_error = z_distance_to_goal
				z_derivative = (z_error - z_previous_error) / dt
				z_integral = z_integral + (z_error * dt)
				z_w = Kp * z_error + Ki * z_integral + Kd * z_derivative
				z_previous_error = z_error

				#ang_error = math.atan2(math.sin(curr_angle-desired_angle), math.cos(curr_angle-desired_angle)) # math.atan2(math.sin(raw_angle_to_goal - curr_angle), math.cos(raw_angle_to_goal - curr_angle))
				#ang_derivative = (ang_error - ang_previous_error) / dt
				#ang_integral = z_integral + (ang_error * dt)
				#ang_w = Kp * ang_error + Ki * ang_integral + Kd * ang_derivative
				#ang_w = math.atan2(math.sin(ang_w), math.cos(ang_w))
				#ang_previous_error = ang_error

				#ang_w = ang_error #* 0.25
				#if(ang_w > 1):
				#	ang_w = 1
				#elif(ang_w < -1):
				#	ang_w = -1
				#elif(abs(math.atan2(math.sin(desired_angle-curr_angle), math.cos(desired_angle-curr_angle))) < math.radians(15)):
				#	ang_w = 0

				vel.linear.x = math.cos(angle_to_goal) * w
				#negative sin due to how Tello interprets roll (right = pos)
				vel.linear.y = -math.sin(angle_to_goal) * w
				vel.linear.z = z_w * 5.5
				vel.angular.z = 0 # ang_w
			
				# max tello speed is +-1
				if(vel.linear.y > 1):
					vel.linear.y = 1
				if(vel.linear.y < -1):
					vel.linear.y = -1
				if(vel.linear.x > 1):
					vel.linear.x = 1
				if(vel.linear.x < -1):
					vel.linear.x = -1
				if(vel.linear.z > 1):
					vel.linear.z = 1
				if(vel.linear.z < -1):
					vel.linear.z = -1

		print("vel.x, vel.y, vel.z: "+ str(vel.linear.x)+", "+ str(vel.linear.y)+", "+ str(vel.linear.z))
		#print("vel.ang.z: "+str(vel.angular.z))
		#print("Kp, Ki, Kd: "+str(Kp)+" "+str(Ki)+" "+str(Kd))
		#print("desired_angle: "+str(math.degrees(desired_angle)))
		#print("angle_error: "+str(math.atan2(math.sin(desired_angle-curr_angle), math.cos(desired_angle-curr_angle))))
		print(strmsg)
		print(str(machine_state))
		print(str(mission_state))
		print(str(warning_state))
		print(str(user_input))
		print(str(command_state))
		h = std_msgs.msg.Header()
		h.stamp = rospy.Time.now()
		headed_str_msg = HeadedString()
		headed_str_msg.header = h
		headed_str_msg.data = str(machine_state)
		machine_state_publisher.publish(headed_str_msg)
		headed_str_msg.data = str(mission_state)
		mission_state_publisher.publish(headed_str_msg)
		headed_str_msg.data = str(warning_state)
		warning_state_publisher.publish(headed_str_msg)
		headed_str_msg.data = str(command_state)
		command_state_publisher.publish(headed_str_msg)
		velocity_publisher.publish(vel)	
		publishing = False
		warning_state = WarningState.Default
		rate.sleep()

if __name__ == "__main__":
    main()
