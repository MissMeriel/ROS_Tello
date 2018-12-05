#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped

goal_x = 1
goal_y = 1
curr_x = 0
curr_y = 0
curr_angle = 0
obs_x = 0
obs_y = 0
obs_z = 0
obs_angle = 0
threshold = 0.07

def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	curr_angle = data.transform.rotation.z
#	curr_angle = math.atan2(math.sin(curr_angle), math.cos(curr_angle))

def vicon_obstacle():
	global obs_x, obs_y, obs_z, obs_angle
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	curr_angle = data.transform.rotation.z

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
	position_subscriber = rospy.Subscriber("vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)

	vel = Twist()
	vel.linear.x = 0.1
	vel.angular.z = 0
	
	set_rate = 1
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	Kp = 0.5 
	Ki = 0.5
	Kd = 0.01
	
	avoid = False
	obstacle_in_path = False
	distance_to_obstacle = sys.float_info.max

	while not rospy.is_shutdown():
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		#obstacle in path if angle of approach == angle of path btwn obstacle & goal
		#and obstacle points are between drone & goal
		angle_of_approach = math.atan((goal_y - curr_y), (goal_x - curr_x))
		angle_obs_to_goal - math.atan((goal_y - obs_y), (goal_x - obst_x))
		obstacle_in_path = abs(angle_of_approach - angle_obs_to_goal) > threshold and (goal_x - obs_x <= goal_x - curr_x) and (goal_y - obs_y <= goal_y - curr_y)
		print("distance to goal: "+ str(distance_to_goal))
		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.angular.z = 0
			print("WITHIN THRESHOLD OF GOAL (" + str(distance_to_goal-threshold)+")")
		else if(obstacle_in_path and distance_to_obstacle < threshold and !avoid):
			print("Obstacle in path")
			answer = raw_input("Avoid obstacle? y/n")
			if("y" not in answer):
				avoid=False
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = 0
			else:
				avoid=True
		else if(avoid):
			#augment path to go around obstacle periphery by some margin
			if((goal_x - obs_x > goal_x - curr_x) and (goal_y - obs_y > goal_y - curr_y)):
				#if obstacle now behind drones current position
		else:
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			x_vel = (goal_x - curr_x) * w
			y_vel = (goal_y - curr_y) * w

			if(x_vel > 1):
				x_vel = 1
			elif (x_vel < -1):
				x_vel = -1
			if(y_vel > 1):
				y_vel = 1
			elif(y_vel < -1):
				y_vel = -1

			print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("x_vel, y_vel: "+ str(x_vel)+", "+ str(y_vel))
			print("")

			vel.linear.x = x_vel
			vel.linear.y = y_vel

			previous_error = error

		velocity_publisher.publish(vel)	
		rate.sleep()

if __name__ == "__main__":
    main()
