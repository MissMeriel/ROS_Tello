#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import Bool
from std_msgs.msg import String
#from vicon_bridge import Markers


goal_x = 1
goal_y = 1
obs_x = -20
obs_y = -20
obs_z = 0
obs_corner_x = 0
obs_corner_y = 0
obs_angle = 0
curr_x = 0
curr_y = 0
curr_angle = 0
threshold = 0.15
publishing = True
avoid = False


def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	#curr_angle = data.transform.rotation.z
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True


def vicon_obstacle(data):
	global obs_x, obs_y, obs_z, obs_angle
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle = data.transform.rotation.z


def obstacle_markers(data):
	#get peripheral points of obstacle and decide which is nearest to current position
	print(data)


def user_input(data):
	global avoid
	if("y" not in answer):
		avoid = False
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = -500
		print("Landing")
	else:
		avoid = True


def main():
	global goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	#obstacle_markers_subscriber = rospy.Subscriber("vicon/markers", Markers, obstacle_markers, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", String, user_input, queue_size=10)

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	str_msg = ""

	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	# Defaults: Kp=0.045; Ki=0.08; Kd=0.075
	Kp = 0.008 
	Ki = 0.03
	Kd = 0.06

	publishing_count = 0
	avoid = False
	ultimate_goal_x = goal_x
	ultimate_goal_y = goal_y
	obstacle_threshold = 0.275
	angle_threshold = 0.15

	while not rospy.is_shutdown():

		print("")
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		#obstacle in path if angle of approach == angle of path btwn obstacle & goal
		#and obstacle points are between drone & goal
		#angle_to_goal handles drone orientation -- adjust x&y velocity
		angle_to_goal = math.atan2(goal_y, goal_x) - curr_angle

		angle_obs_to_goal = math.atan2((goal_y - obs_y), (goal_x - obs_x))
		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		print("curr_angle: "+ str(curr_angle))
		#print("angle_obs_to_goal: "+str(angle_obs_to_goal))

		obstacle_in_path = abs(angle_to_goal - angle_obs_to_goal) < angle_threshold and ((abs(obs_x - curr_x) < obstacle_threshold) or (abs(obs_y - curr_y) < obstacle_threshold))
		print("obstacle_in_path: "+str(obstacle_in_path))

		#print("distance to obstacle: "+ str(distance_to_obstacle))
		str_msg = "distance to goal: "+ str(distance_to_goal)

		obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			print("WITHIN THRESHOLD OF GOAL (" + str(distance_to_goal-threshold)+")")
			str_msg = "WITHIN THRESHOLD OF GOAL (" + str(distance_to_goal)+")"
		else:

			#if(obstacle_in_path and distance_to_obstacle < threshold and not avoid):
			if(obstacle_in_path and distance_to_obstacle < threshold and not avoid):
				print("OBSTACLE_IN_PATH")
				str_msg = "Obstacle in path"
				#hover while waiting for user input
				vel.linear.x = 0
				vel.linear.y = 0
				sent = 0
				while(sent < 5):
					velocity_publisher.publish(vel)
					sent += 1

			elif(obstacle_in_path and avoid):
				print("OBSTACLE_IN_PATH; AVOID")
				str_msg = "Obstacle in path; avoiding"
				#interpolated goal offset from obstacle radius
				if(curr_angle < 0):
					goal_x = math.cos(curr_angle-threshold) * 3
				else:
					goal_x = math.cos(curr_angle+threshold) * 3
				goal_y = curr_y
				error = 0
				integral = 0
				previous_error = 0
				
			elif(avoid and not obstacle_in_path):
				goal_x = ultimate_goal_x
				goal_y = ultimate_goal_y
				avoid = False
				print("OBSTACLE NOT IN_PATH; RESUME TOWARDS GOAL")

			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			#print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			#print("curr_angle: " + str(curr_angle))
			#print("x_vel, y_vel: "+ str(x_vel)+", "+ str(y_vel))
			print("actual vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))

			vel.linear.x = math.cos(angle_to_goal) * w 
			vel.linear.y = -math.sin(angle_to_goal) * w

			# max tello speed is +-1
			if(vel.linear.y > 1):
				vel.linear.y = 1
			if(vel.linear.y < -1):
				vel.linear.y = -1
			if(vel.linear.x > 1):
				vel.linear.x = 1
			if(vel.linear.x < -1):
				vel.linear.x = -1

			# account for deadzone below 0.1
			if(abs(vel.linear.x) < 0.08):
				vel.linear.x *= 1.5
			elif(abs(vel.linear.x) < 0.01):
				vel.linear.x *= 9

			if(abs(vel.linear.y) < 0.08):
				vel.linear.y *= 1.5
			elif(abs(vel.linear.y) < 0.01):
				vel.linear.y *= 9

			previous_error = error

		#check that we haven't gone too long without vicon data
		if(not publishing):
			publishing = False
			publishing_count += 1
		else:
			publishing_count = 0
			publishing = True
		if(publishing_count > 2):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -500
			print("NO VICON DATA; LANDING")
			str_msg = "NO VICON DATA; LANDING"

		print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		print("goal: "+str(goal_x)+", "+str(goal_y))
		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()

if __name__ == "__main__":
    main()
