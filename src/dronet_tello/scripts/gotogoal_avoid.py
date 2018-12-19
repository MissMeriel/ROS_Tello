#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import String

goal_x = 1
goal_y = 1
obs_x = 0
obs_y = 0
obs_z = 0
obs_corner_x = 0
obs_corner_y = 0
obs_angle = 0
curr_x = 0
curr_y = 0
curr_z = 0
curr_angle = 0
threshold = 0.12


def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	#curr_angle = data.transform.rotation.z
	#curr_angle = math.atan2(math.sin(curr_angle), math.cos(curr_angle))
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);


def vicon_obstacle(data):
	global obs_x, obs_y, obs_z, obs_angle
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle = data.transform.rotation.z


def obstacle_markers(data):
	#get peripheral points of obstacle and decide which is nearest to current position
	print(data)

def main():
	global goal_x, goal_y
	global obs_x, obs_y, obs_z, obs_angle
	global threshold
	global curr_x, curr_y, curr_angle
	rospy.init_node("gotogoal_avoid", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	obstacle_markers_subscriber = rospy.Subscriber("vicon/OBSTACLE/Markers", TransformStamped, obstacle_markers, queue_size=10)

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	str_msg = ""
	
	#TODO lower set_rate
	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	Kp = 0.1 
	Ki = 0.017
	Kd = 0.1

#	These kinda work:
	Kp = 0.045 
	Ki = 0.08
	#ratchet down Kd
	Kd = 0.1#0.075

	avoid = False
	obstacle_in_path = False
	distance_to_obstacle = sys.float_info.max
	ultimate_goal_x = goal_x
	ultimate_goal_y = goal_y

	while not rospy.is_shutdown():

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		print("")		
		print("distance to goal: "+ str(distance_to_goal))
		distance_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		#obstacle in path if angle of approach == angle of path btwn obstacle & goal
		#and obstacle points are between drone & goal
		angle_of_approach = math.atan2((goal_y - curr_y), (goal_x - curr_x))
		angle_obs_to_goal = math.atan2((goal_y - obs_y), (goal_x - obs_x))
		obstacle_in_path = abs(angle_of_approach - angle_obs_to_goal) > threshold and (goal_x - obs_x <= goal_x - curr_x) and (goal_y - obs_y <= goal_y - curr_y)
		print("distance to obstacle: "+ str(distance_to_obstacle))
		str_msg = "distance to goal: "+ str(distance_to_goal)

		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.linear.y = 0
			print("WITHIN THRESHOLD OF GOAL (" + str(distance_to_goal-threshold)+")")
			str_msg = "WITHIN THRESHOLD OF GOAL (" + str(distance_to_goal)+")"
		else:

			if(obstacle_in_path and distance_to_obstacle < threshold and not avoid):
				print("Obstacle in path")
				str_msg = "Obstacle in path"
				#user input
				#TODO: add timeout
				answer = raw_input("Avoid obstacle? y/n")
				if("y" not in answer):
					avoid=False
					vel.linear.x = 0
					vel.linear.y = 0
					vel.linear.z = 0
					str_msg += "; Landing"
				else:
					avoid=True
			elif(obstacle_in_path and avoid):
				#interpolated goal offset from obstacle radius
				#if():
				goal_x = obs_corner_x + 1
				goal_y = curr_y
				error = 0
				integral = 0
				previous_error = 0
				#else:
				#goal_x = obs_corner_x + 1
				#goal_y = obs_corner_y + 1
			elif(avoid and not obstacle_in_path):
				goal_x = ultimate_goal_x
				goal_y = ultimate_goal_y
				avoid = False

			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			x_vel = (goal_x - curr_x) * w
			y_vel = -(goal_y - curr_y) * w
			vel.linear.x = x_vel
			vel.linear.y = y_vel

			print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("curr_angle: " + str(curr_angle))
			print("x_vel, y_vel: "+ str(x_vel)+", "+ str(y_vel))

			previous_error = error

		velocity_publisher.publish(vel)	
		state_publisher.publish(str_msg)
		rate.sleep()

if __name__ == "__main__":
    main()
