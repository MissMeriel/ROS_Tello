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
curr_y = 0#-5
curr_angle = 0#-0.7853981633974483
goal_x = -5#1
goal_y = 5#1
counter = 0
threshold = 0.1
dt = 20

def plot_x():
	global curr_x, curr_y, counter
	plt.plot(goal_x, goal_y, '*')
	#if counter % 10 == 0:
	plt.plot(curr_x, curr_y, 'ro')
	plt.axis("equal")
	plt.draw()
	plt.pause(0.00000000001)
	counter += 1

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle

	integral = 0
	previous_error = 0

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode:  Kp = 0.03; Ki = 0.003; Kd = 0.006
	Kp = 0.01
	Ki = 0.00003
	Kd = 0.003

	xvels = []
	yvels = []
	ws = []
	while(True):
		
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		print("")
		print("distance to goal: "+ str(distance_to_goal))
		angle_to_goal = math.atan2(goal_y-curr_y, goal_x-curr_x)# - curr_angle
#		print("angle_to_goal with offset: "+str(math.degrees(math.atan2(goal_y-curr_y, goal_x-curr_y)- curr_angle)))
		print("angle_to_goal: "+str(math.degrees(angle_to_goal)))
		#print("angle_to_goal: "+ str(angle_to_goal))
		if (distance_to_goal < threshold):
			#vel_x = 0
			#vel_y = 0
			print("Goal reached within threshold: " + str(distance_to_goal))
			#print(xvels)
			#print(yvels)
			print(ws)
			#time.sleep(10)
		else:
			error = distance_to_goal
			#error = error * np.sign(math.sin(angle_to_goal))
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

		time.sleep(0.2)

	
if __name__ == "__main__":
    main()
