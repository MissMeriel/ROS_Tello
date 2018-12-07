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

curr_x = -5
curr_y = -5
curr_angle = 0#-0.7853981633974483
goal_x = 3
goal_y = 3
obs_x = 0
obs_y = 0
obs_radius = 1
counter = 0
threshold = 0.1
dt = 20

def plot_x():
	global curr_x, curr_y, counter
	plt.plot(goal_x, goal_y, '*')
	plt.plot(obs_x, obs_y, 'g^')
	#if counter % 10 == 0:
	plt.plot(curr_y, curr_x, 'ro')
	plt.axis("equal")
	plt.draw()
	plt.pause(0.00000000001)
	counter += 1

def main():
	global goal_x, goal_y
	global obs_x, obs_y
	global threshold
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
	obstacle_threshold = 0.275
	angle_threshold = 0.15
	detection_distance = 3
	avoid = False

	while(True):
		
		print("")

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)

		distance_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		angle_obs_to_goal = math.atan2((goal_y - obs_y), (goal_x - obs_x))
		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		#print("curr_angle: "+ str(curr_angle))

		angle_to_goal = math.atan2(goal_y-curr_y, goal_x-curr_x) - curr_angle
		angle_drone_to_goal = math.atan2(goal_y-curr_y, goal_x-curr_x)
		print("distance to goal: "+ str(distance_to_goal))
		#print("angle_to_goal: "+str(math.degrees(angle_to_goal)))
		#print("angle_drone_to_goal: "+str(math.degrees(angle_drone_to_goal)))
		obstacle_in_path = abs(angle_drone_to_goal - angle_obs_to_goal) < angle_threshold and ((abs(obs_x - curr_x) < detection_distance) or (abs(obs_y - curr_y) < detection_distance))
		print("obstacle_in_path: "+str(obstacle_in_path))

		if (distance_to_goal < threshold):
			#Hover then land
			#vel_x = 0
			#vel_y = 0
			print("Goal reached within threshold: " + str(distance_to_goal))
			time.sleep(10)
		elif(obstacle_in_path and not avoid and distance_to_obstacle < threshold):
			print("OBSTACLE_IN_PATH")
			#hover while waiting for user input
			vel_x = 0
			vel_y = 0
			time.sleep(2)
			avoid = True
			print("avoid_goal: "+str(goal_x)+", "+str(goal_y))
		elif(obstacle_in_path and avoid):
			print("OBSTACLE_IN_PATH; AVOID")
			#interpolated goal offset from obstacle radius
			avoid_angle = angle_drone_to_goal + math.radians(45)
			#obs radius + distance threshold *2
			#goal_x = 3 * math.cos(avoid_angle)
			#goal_y = 3 * math.sin(avoid_angle)

			goal_x = obs_x #+ math.cos(angle_obs_to_goal) * 10
			goal_y = obs_y + 2 #math.sin(angle_obs_to_goal) * 10
			#if(curr_angle < 0):
			#	goal_x = math.cos(curr_angle-threshold) * 3
			#else:
			#	goal_x = math.cos(curr_angle+threshold) * 3
			#goal_y = curr_y

			
		elif(not avoid):
			if(obstacle_in_path):
				#pi + angle drone to goal
				angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
				hover_point_x = obs_x + math.cos(angle_obs_to_drone)
				hover_point_y = obs_y + math.sin(angle_obs_to_drone)
				goal_x = hover_point_x
				goal_y = hover_point_y
				print("goal set to hover_point: "+str(hover_point_x)+", "+str(hover_point_y))
				error = 0
				integral = 0
				previous_error = 0
				#avoid = True

			else:
				goal_x = final_goal_x
				goal_y = final_goal_y
				avoid = False
				print("OBSTACLE NOT IN_PATH; GO TOWARDS GOAL")

				error = distance_to_goal
				#error = error * np.sign(math.sin(angle_to_goal))
				derivative = (error - previous_error) / dt
				integral = integral + (error * dt)
				w = Kp*error + Ki*integral + Kd*derivative

				vel_x = math.cos(angle_to_goal) * w
				#negative sin due to how Tello interprets roll (left = pos)
				vel_y = math.sin(angle_to_goal) * w

				previous_error = error

				print("w: "+str(w))
				print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
				#print("curr_angle: " + str(curr_angle))
				#print("angle_to_goal: " + str(angle_to_goal))
				print("actual vel.x, vel.y: "+ str(vel_x)+", "+ str(vel_y))
			
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
		#curr_x = curr_x + vel_x*math.cos(curr_angle) + vel_y*math.cos(curr_angle)
		#curr_y = curr_y + vel_x*math.sin(curr_angle) + vel_y*math.sin(curr_angle)

		plot_x()

		time.sleep(0.2)

	
if __name__ == "__main__":
    main()
