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

curr_x = -1
curr_y = -1
curr_angle = 0#-0.7853981633974483
goal_x = [0, 0.5, 0, 2]
goal_y = [0, -1.5, 1, 1.5]
#obs_x = [-0.5, 0.25]
#obs_y = [-0.5, -1]
obs_x = -0.5
obs_y = -0.5
goal_counter = 0
threshold = 0.05
dt = 2

def plot_x():
	global curr_x, curr_y, goal_x, goal_y, goal_counter, threshold
	plt.plot(goal_x, goal_y, '*')
	plt.plot(obs_x, obs_y, 'go')
	#if counter % 10 == 0:
	plt.plot(curr_x, curr_y, 'ro')
	distance_to_goal = math.sqrt((goal_x[goal_counter] - curr_x)**2 + (goal_y[goal_counter] - curr_y)**2)
	if(distance_to_goal < threshold):
		x=goal_x[goal_counter]
		y= goal_y[goal_counter]
		plt.annotate("Reached "+str(x)+","+str(y), (x,y))
	if(goal_counter == len(goal_x)-1 and distance_to_goal < threshold):
		plt.annotate("LANDING", (goal_x[goal_counter], goal_y[goal_counter]))
	plt.axis("equal")
	plt.draw()
	plt.pause(0.00000000001)


def main():
	global goal_x, goal_y
	global threshold
	global goal_counter
	global curr_x, curr_y, curr_angle, dt

	integral = 0
	previous_error = 0

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode:  Kp = 0.03; Ki = 0.003; Kd = 0.006
	# Sim values:  Kp = 0.01; Ki = 0.00003; Kd = 0.003
	Kp = 0.07
	Ki = 0.00003
	Kd = 0.03
	goal_counter = 0
	xvels = []
	yvels = []
	ws = []
	avoid_count = 0
	while(True):	
		distance_to_goal = math.sqrt((goal_x[goal_counter] - curr_x)**2 + (goal_y[goal_counter] - curr_y)**2)
		obs_to_goal = math.sqrt((goal_x[goal_counter] - obs_x)**2 + (goal_y[goal_counter] - obs_y)**2)
		distance_to_obs = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		angle_to_goal = math.atan2(goal_y[goal_counter] - curr_y, goal_x[goal_counter] - curr_x)
		angle_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		obstacle_in_path = abs(angle_to_goal - angle_to_obs) < 0.5 and distance_to_goal > obs_to_goal and distance_to_obs < 0.3
		avoid = obstacle_in_path or (avoid_count < 5 and avoid_count > 1)
		print("")
		print("distance to goal: "+ str(distance_to_goal))
		print("angle_to_goal: "+str(math.degrees(angle_to_goal)))
		print("obs_in_path: "+str(obstacle_in_path))
		if (distance_to_goal < threshold):
			#vel_x = 0
			#vel_y = 0
			print("Goal reached with threshold: " + str(distance_to_goal))
			goal_counter += 1
			integral = 0
			previous_error = 0
			#print(xvels)
			#print(yvels)
			#print(ws)
			time.sleep(3)
			if(goal_counter > len(goal_x)-1):
				print("LANDING")
				exit()
		elif(avoid):
			#find tangent line for velocity vector
			avoid_angle = math.atan2(obs_y-curr_y, obs_x-curr_x) + math.pi/2.0
			print("avoid angle: "+str(math.degrees(avoid_angle)))
			vel_x = math.cos(avoid_angle) * 0.1
			vel_y = math.sin(avoid_angle) *0.1
			avoid_count += 1
		#elif(avoid and obstacle2):
			
		else:
			avoid_count = 0
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative
			ws.append(w)

			vel_x = math.cos(angle_to_goal) * w
			vel_y = math.sin(angle_to_goal) * w

			previous_error = error

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
		xvels.append(vel_x)
		yvels.append(vel_y)
		plot_x()

		time.sleep(0.002)

	
if __name__ == "__main__":
    main()
