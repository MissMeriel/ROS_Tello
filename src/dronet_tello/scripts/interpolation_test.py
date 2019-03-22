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
import rosgraph.impl.graph as rig
from matplotlib import pyplot as plt

#take in form of x1,x2,x3,x4
goal_x = sys.argv[1]
goal_y = sys.argv[2]
interpolation_x = [0]
interpolation_y = [0]
curr_x = 0
curr_y = 0
curr_angle = 0
threshold = 0.1
publishing = True
kill = False

def process_sysargs():
	global goal_x, goal_y, interpolation_x, interpolation_y, curr_x, curr_y
	goal_x = goal_x.split(",")
	goal_y = goal_y.split(",")
	for i in range(0,len(goal_x)):
		goal_x[i] = float(goal_x[i])
		goal_y[i] = float(goal_y[i])
	print("goal_x: "+str(goal_x))
	print("goal_y: "+str(goal_y))
	# pick closer goal, make first entry in interpolations
	distance_1 = math.sqrt((curr_x-goal_x[0])**2+(curr_y-goal_y[0])**2)
	distance_2 = math.sqrt((curr_x-goal_x[1])**2+(curr_y-goal_y[1])**2)
	if(distance_1 < distance_2):
		print(goal_x[0])
		print(len(interpolation_x))
		interpolation_x[0] = goal_x[0]
		interpolation_y[0] = goal_y[0]
	else:
		interpolation_x[0] = goal_x[1]
		interpolation_y[0] = goal_y[1]
		goal_x[1] = goal_x[0]
		goal_y[1] = goal_y[0]
		goal_x[0] = interpolation_x[0]
		goal_y[0] = interpolation_y[0]
	print("interpolation_x: "+str(interpolation_x))
	print("interpolation_y: "+str(interpolation_y))
	# interpolate
	interpolate(0.2)

def interpolate(increment_x):
	global goal_x, goal_y, interpolation_x, interpolation_y
	index = 2
	print("increment_x: "+str(increment_x))
	for i in frange(goal_x[0], goal_x[1], increment_x):
		interpolation_x.append(i)
		if(index % 2 == 0 or i == goal_x[1]):
			interpolation_y.append(goal_y[1])
		else:
			interpolation_y.append(goal_y[0])
		index += 1
	if(interpolation_y[len(interpolation_y)-1] == goal_y[1]):
		# need one more traverse
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[0])
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[1])
	else:
		interpolation_x.append(goal_x[1])
		interpolation_y.append(goal_y[1])
	print("interpolation_x: "+str(interpolation_x))
	print("interpolation_y: "+str(interpolation_y))
	plot_x(interpolation_x, interpolation_y)

def plot_x(x, y):
	plt.plot(x[0], y[0], 'r^')
	plt.plot(x, y, 'r-')
	plt.plot(x[len(x)-1], y[len(y)-1], 'g^')
	plt.axis("equal")
	plt.draw()
	plt.pause(10)

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
	#yield stop

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	global publishing, kill

	process_sysargs()
	print("Processed args")

if __name__ == "__main__":
    main()
