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
threshold = 0.2

def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	#curr_angle = data.transform.rotation.z
	#curr_angle = math.atan2(math.sin(curr_angle), math.cos(curr_angle))
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	set_rate = 1200
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
	Kd = 0.075

	while not rospy.is_shutdown():

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		print("")		
		print("distance to goal: "+ str(distance_to_goal))

		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.linear.y = 0
			print("~~`~``~~````~~!~~````~~``~`~~")
			print("~~`~``~~````!!!!!````~~``~`~~")
			print("GOOOOooooooOOOOOOOOOoooAAAAL!")
			print("~~`~``~~````!!!!!````~~``~`~~")
			print("~~`~``~~````~~!~~````~~``~`~~")
		else:
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			x_vel = (goal_x - curr_x) * w
			y_vel = -(goal_y - curr_y) * w

			print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("curr_angle: " + str(curr_angle))
			print("x_vel, y_vel: "+ str(x_vel)+", "+ str(y_vel))

			previous_error = error

		velocity_publisher.publish(vel)	
		rate.sleep()

if __name__ == "__main__":
    main()
