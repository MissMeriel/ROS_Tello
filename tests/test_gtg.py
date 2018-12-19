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

curr_x = -10
curr_y = -10
curr_angle = 0#-0.7853981633974483
goal_x = [-5, 3, -1, 3]
goal_y = [-5, -10, 1, 3]
goal_counter = 0
threshold = 0.1
dt = 2

def plot_x():
	global curr_x, curr_y, goal_counter
	plt.plot(goal_x, goal_y, '*')
	#if counter % 10 == 0:
	plt.plot(curr_x, curr_y, 'ro')
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
	Kp = 0.01
	Ki = 0.00003
	Kd = 0.003
	goal_counter = 0
	xvels = []
	yvels = []
	ws = []
	while(True):	
		distance_to_goal = math.sqrt((goal_x[goal_counter] - curr_x)**2 + (goal_y[goal_counter] - curr_y)**2)
		print("")
		print("distance to goal: "+ str(distance_to_goal))
		angle_to_goal = math.atan2(goal_y[goal_counter] - curr_y, goal_x[goal_counter] - curr_x)# - curr_angle
		print("angle_to_goal: "+str(math.degrees(angle_to_goal)))
		if (distance_to_goal < threshold):
			#vel_x = 0
			#vel_y = 0
			print("Goal reached with threshold: " + str(distance_to_goal))
			goal_counter += 1
			if(goal_counter > len(goal_x)-1):
				print("LANDING")
				exit()
			integral = 0
			previous_error = 0
			#print(xvels)
			#print(yvels)
			#print(ws)
			time.sleep(3)
		else:
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			print("p: "+str(Kp*error))
			print("i: "+str(Ki*integral))
			print("d: "+str(Kd*derivative))
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative
			ws.append(w)

			vel_x = math.cos(angle_to_goal) * w
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
		xvels.append(vel_x)
		yvels.append(vel_y)
		#curr_x = curr_x + vel_x*math.cos(curr_angle) + vel_y*math.cos(curr_angle)
		#curr_y = curr_y + vel_x*math.sin(curr_angle) + vel_y*math.sin(curr_angle)

		plot_x()

		time.sleep(0.002)

	
if __name__ == "__main__":
    main()
