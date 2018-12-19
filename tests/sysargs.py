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

goal_x = sys.argv[1]
goal_y = sys.argv[2]

def main():
	global goal_x, goal_y
	print(goal_x)
	print(goal_y)
	goal_x = goal_x.split(",")
	goal_y = goal_y.split(",")
	print(goal_x)
	print(goal_y)
	for i in range(0,len(goal_x)):
		goal_x[i] = int(goal_x[i])
		goal_y[i] = int(goal_y[i])
	print(goal_x)
	print(goal_y)

if __name__ == "__main__":
	main()
