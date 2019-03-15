#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from dronet_tello.msg import FlightData
from dronet_tello.msg import HeadedBool 
import rosgraph.impl.graph as rig


#take in form of x1,x2,x3,x4...
goal_x = sys.argv[1]
goal_y = sys.argv[2]
goal_z = sys.argv[3]
interpolation_x = []
interpolation_y = []
curr_x = 0
curr_y = 0
curr_z = 0
curr_angle = 0
home_x = 0
home_y = 0
threshold = 0.1
publishing = True
kill = False
sweeping = False
possible_target_detected = False
old_height = 0


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
		interpolation_x[0] = goal_x[0]
		interpolation_y[0] = goal_y[0]
		interpolation_z[0] = goal_z[0]
	else:
		interpolation_x[0] = goal_x[1]
		interpolation_y[0] = goal_y[1]
		interpolation_z[0] = goal_z[1]
		goal_x[1] = goal_x[0]
		goal_y[1] = goal_y[0]
		goal_z[1] = goal_z[0]
		goal_x[0] = interpolation_x[0]
		goal_y[0] = interpolation_y[0]
		goal_z[0] = interpolation_z[0]
	# interpolate
	interpolate(0.2)


# Assuming constant y coordinates
def interpolate(increment_z):
	global goal_x, goal_y, goal_z, interpolation_x, interpolation_y, interpolation_z
	index = 2
	for i in frange(goal_x[0], goal_x[1], increment_x):
		interpolation_x.append(i)
		if(index % 2 == 0 or i == goal_x[1]):
			interpolation_z.append(goal_z[1])
		else:
			interpolation_z.append(goal_z[0])
		interpolation_y.append(goal_y[0])
		index += 1
	if(interpolation_z[len(interpolation_z)-1] == goal_z[1]):
		# need one more traverse
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[0])
		interpolation_z.append(goal_z[0])
	interpolation_x.append(goal_x[1])
	interpolation_y.append(goal_y[1])
	interpolation_z.append(goal_z[0])


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


def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global home_x, home_y
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	curr_z = data.transform.translation.z
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True
	if(curr_z < 0.01):
		home_x = data.transform.translation.x
		home_y = data.transform.translation.y


def process_user_input(data):
	global kill
	if("cancel" in str(data).lower()):
		kill=True


def process_flight_data(data):
	global sweeping, possible_target_detected, old_height
	# height == VPS data
	if(sweeping and old_height - data.height > 1):
		possible_target_detected = True


def main():
	global goal_x, goal_y, interpolation_x, interpolation_y
	global threshold
	global curr_x, curr_y, curr_angle
	global publishing, kill, sweeping

	process_sysargs()

	rospy.init_node("sweep", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=1)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", String, process_user_input, queue_size=5)
	flight_data_subscriber = rospy.Subscriber("/flight_data", String, process_flight_data, queue_size=5)

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

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode: Kp = 0.03; Ki = 0.003; Kd = 0.006
	Kp = 0.41
	Ki = 0.003
	Kd = 0.01
	publishing_count = 0
	hover_count = 0
	goal_counter = 0

	#if(interpolation_x(len(interpolation_x)-1) ~= home_x and interpolation_y(len(interpolation_y)-1) ~= home_y)
		#interpolation_x.append(home_x)
		#interpolation_y.append(home_y)
		#interpolation_z.append(1)

	while not rospy.is_shutdown():

		#3D Euclidean distance
		distance_to_goal = math.sqrt((interpolation_x[goal_counter] - curr_x)**2 + (interpolation_y[goal_counter] - curr_y)**2)
		z_distance_to_goal = interpolation_z[goal_counter] - curr_z
		print("")
		#percent_mission_completed = percent_mission_completed()
		#print("% completed: "+ str(distance_to_goal)+"%")
		angle_to_goal = math.atan2(goal_y[goal_counter]-curr_y, goal_x[goal_counter]-curr_x) - curr_angle
		raw_angle_to_goal = math.atan2(goal_y[goal_counter]-curr_y, goal_x[goal_counter]-curr_x)

		# check for lapse in vicon data
		if(not publishing):
			publishing_count += 1
		else:
			publishing_count = 0
		if(publishing_count > 5):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			str_msg = "NO VICON DATA"
			print(str_msg)
			state_publisher.publish(str_msg)
			velocity_publisher.publish(vel)
			continue

		#finished sweeping
		if (distance_to_goal < threshold and z_distance_to_goal < threshold and interpolation_x[goal_counter] == goal_x[1] and interpolation_x[goal_counter] == goal_y[1] and interpolation_z[goal_counter] == goal_z[1]):
			#query user for options: Sweep again? Inspect specific point? Go home?
			if(hover_count > 2):
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				velocity_publisher.publish(vel)
				state_publisher.publish("Finished behavior")
			elif(hover_count > 2 and goal_counter == len(goal_x)-1):
				exit()
			elif(hover_count > 2 and goal_counter < len(goal_x)-1):
				#exit_count = 0
				hover_count = 0
				integral = 0
				previous_error = 0
				goal_counter +=1

		#reached sweeping area
		elif (distance_to_goal < threshold and z_distance_to_goal < threshold and interpolation_x[goal_counter] == goal_x[0] and interpolation_x[goal_counter] == goal_y[0] and interpolation_z[goal_counter] == goal_z[0]):
				vel.linear.x = 0
				vel.linear.y = 0
				strmsg = "SWEEP AREA REACHED"
			if(hover_count > 2 and goal_counter == len(interpolation_x)-1):
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				strmsg = "Finished sweep"
				#interpolation_x.append(home_x)
				#interpolation_y.append(home_y)
				#interpolation_z.append(1)
				#goal_counter += 1
			print(strmsg)
			velocity_publisher.publish(vel)
			state_publisher.publish(strmsg)
			hover_count += dt

		#reached an interpolated goal
		elif (distance_to_goal < threshold and z_distance_to_goal < threshold):
			#reached sweep area
			if(hover_count < 2 and goal_counter < len(interpolation_x)-1):
				vel.linear.x = 0
				vel.linear.y = 0
				strmsg = "SWEEPING; REACHED INTERPOLATION POINT"
			elif(hover_count > 2 and goal_counter < len(interpolation_x)-1):
				vel.linear.x = 0
				vel.linear.y = 0
				strmsg = "SWEEPING; LEAVING INTERPOLATION POINT"
				hover_count = 0
				integral = 0
				previous_error = 0
				z_integral = 0
				z_previous_error = 0
				goal_counter += 1
			print(strmsg)
			velocity_publisher.publish(vel)
			state_publisher.publish(strmsg)
			hover_count += dt

		elif(kill):
			#send land cmd then exit
			print("User requested land")
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			velocity_publisher.publish(vel)
			state_publisher.publish("User requested land")
			exit_count+= 1
			if(exit_count > 5):
				exit()
		else:
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative
			previous_error = error

			z_error = z_distance_to_goal
			z_derivative = (z_error - z_previous_error) / dt
			z_integral = z_integral
			z_w = Kp * z_error + Ki * z_integral + Kd * z_derivative
			z_previous_error = z_error

			ang_error = math.atan2(math.cos(raw_angle_to_goal - curr_angle), math.sin(raw_angle_to_goal - curr_angle))
			ang_w = ang_error
			if(ang_w > 1):
				ang_w = 1
			elif(ang_w < -1):
				ang_w = -1

			vel.linear.x = math.cos(angle_to_goal) * w
			#negative sin due to how Tello interprets roll (right = pos)
			vel.linear.y = -math.sin(angle_to_goal) * w
			vel.linear.z = z_w
			vel.angular.x = ang_w

			print("curr_x, curr_y, curr_z: "+str(curr_x)+", "+str(curr_y)+", "+str(curr_z))
			
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

			if(goal_counter > 0):
				strmsg = "SWEEPING"
			else:
				strmsg = "APPROACHING/LEAVING SWEEP AREA"

		print("vel.x, vel.y, vel.z: "+ str(vel.linear.x)+", "+ str(vel.linear.y)+", "+ str(vel.linear.z))
		state_publisher.publish(strmsg)
		velocity_publisher.publish(vel)	
		publishing = False
		rate.sleep()

if __name__ == "__main__":
    main()
