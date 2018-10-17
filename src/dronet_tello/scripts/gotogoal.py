#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback

from geometry_msgs.msg import Twist

goal_x = 1
goal_y = 1
threshold = 0.1

def vicon_data(data):
	curr_x = data.linear.x
	curr_y = data.linear.y
	curr_z = data.linear.z

def main:
	global goal
	global threshold
	velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
	position_subscriber = rospy.Subscriber("vicon", transform, queue_size=10)

	vel = Twist()
	vel.linear.x = 0.1 
	vel.angular.z = 0
	
	set_rate = 10
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	Kp = 1
	Ki = 0
	Kd = 0
	while not rospy.is_shutdown():
		distance_to_goal = sqrt((goal_x -curr_x)^2 + (goal_y - curr_y)^2)
		angular_error = 
		derivative = (error - previous_error) / dt
		integral = integral + (error * dt)
		w = Kp*error + Ki*integral + Kd*derivative
		previous_error = error
		
		if ():

if __name__ == "__main__":
    main()
