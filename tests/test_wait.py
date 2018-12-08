#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
import numpy as np
from threading import Thread
from matplotlib import pyplot as plt

curr_x = 2
curr_y = 2
curr_angle = 0#-0.7853981633974483
goal_x = -3
goal_y = -3
obs_x = 0
obs_y = 0
obs_radius = 1
counter = 0
threshold = 0.15
dt = 1.0/20.0

def plot_x():
	global curr_x, curr_y
	global goal_x, goal_y
	plt.plot(goal_x, goal_y, '*')
	plt.plot(obs_x, obs_y, 'g^')
	plt.plot(curr_y, curr_x, 'ro')
	plt.axis("equal")
	plt.draw()
	plt.pause(0.00000000001)

def main():
	global goal_x, goal_y
	global obs_x, obs_y
	global threshold, dt
	global curr_x, curr_y, curr_angle

	integral = 0
	previous_error = 0

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode:  Kp = 0.01; Ki = 0.0003; Kd = 0.0006
	Kp = 0.01 
	Ki = 0.0003
	Kd = 0.0006

	final_goal_x = goal_x
	final_goal_y = goal_y
	obstacle_threshold = 0.2
	angle_threshold = 0.15
	detection_distance = 1
	avoid = False
	count = 0.0
	vel_x = 0
	vel_y = 0
	hover_count = 0

	while(True):
		
		print("")

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)
		distance_drone_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)

		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		angle_obs_to_goal = math.atan2((goal_y - obs_y), (goal_x - obs_x))
		angle_drone_to_goal = math.atan2(goal_y-curr_y, goal_x-curr_x)

		paths_align = abs(angle_drone_to_goal - angle_obs_to_goal) < angle_threshold
		obstacle_in_path = paths_align and distance_drone_to_obstacle < detection_distance
		print("angle_drone_to_goal: "+str(math.degrees(angle_drone_to_goal)))
		print("angle_obs_to_goal: "+str(math.degrees(angle_obs_to_goal)))
		print("obstacle_in_path: "+str(obstacle_in_path))
		print("distance to goal: "+ str(distance_to_goal))
		print("distance to obstacle: "+ str(distance_drone_to_obstacle))

		if (distance_to_final_goal < threshold):
			#Hover then land
			print("GOAL REACHED within threshold: " + str(distance_to_goal))
			time.sleep(10)

		else:
			print("NOT @ FINAL GOAL")
			if(obstacle_in_path):
				print("AND OBS IIN PATH")
				angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
				print("angle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
				hover_point_x = obs_x + obstacle_threshold * math.cos(angle_obs_to_drone)
				hover_point_y = obs_y + obstacle_threshold * math.sin(angle_obs_to_drone)
				goal_x = hover_point_x
				goal_y = hover_point_y
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))
				print("GOAL @ HOVER POINT: "+str(hover_point_x)+", "+str(hover_point_y))

				#error = 0
				#integral = 0
				#previous_error = 0
				if(abs(distance_to_goal-obstacle_threshold) <= threshold and hover_count < 5):
					vel_x=0
					vel_y=0
					print("@ HOVERPOINT; PREPARING TO AVOID")
					avoid = True
					hover_count += 1
			else:
				goal_x = final_goal_x
				goal_y = final_goal_y
				print("OBSTACLE NOT IN_PATH; GO TOWARDS GOAL")

			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			vel_x = math.cos(angle_drone_to_goal) * w
			vel_y = math.sin(angle_drone_to_goal) * w

			previous_error = error

			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			#print("w: "+str(w))
			#print("actual vel.x, vel.y: "+ str(vel_x)+", "+ str(vel_y))
			print("curr_angle: " + str(curr_angle))
			print("angle_drone_to_goal: " + str(angle_drone_to_goal))

		
			# max tello speed is +-1
			if(vel_y > 1):
				vel_y = 1
			if(vel_y < -1):
				vel_y = -1
			if(vel_x > 1):
				vel_x = 1
			if(vel_x < -1):
				vel_x = -1

		print("vel.x, vel.y: "+ str(vel_x)+", "+ str(vel_y))
		curr_x = curr_x + vel_x
		curr_y = curr_y + vel_y

		plot_x()

		time.sleep(0.05)

	
if __name__ == "__main__":
    main()
