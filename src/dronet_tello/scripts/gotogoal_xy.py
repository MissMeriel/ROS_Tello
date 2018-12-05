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
threshold = 0.07

def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
#	curr_angle = data.transform.rotation.z
	curr_angle = math.tan(curr_y/curr_x)
	curr_angle = math.atan2(math.sin(curr_angle), math.cos(curr_angle))

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
	position_subscriber = rospy.Subscriber("vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)

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

	integral_d = 0
	error_d = 0
	previous_error_d = 0
	Kp_d = 0.9
	Ki_d = 0
	Kd_d = 0

	while not rospy.is_shutdown():
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		print("distance to goal: "+ str(distance_to_goal))
		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.angular.z = 0
			print("~~`~``~~````~~!~~````~~``~`~~")
			print("~~`~``~~````!!!!!````~~``~`~~")
			print("GOOOOooooooOOOOOOOOOoooAAAAL!")
			print("~~`~``~~````!!!!!````~~``~`~~")
			print("~~`~``~~````~~!~~````~~``~`~~")
		else:
#			desired_angle = math.atan2(goal_y-curr_y, goal_x-curr_x)
#			print("desired angle: "+str(desired_angle))
#			error = desired_angle - curr_angle
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

#			error_d = distance_to_goal
#			derivative_d = (error_d - previous_error_d) / dt
#			integral_d = integral_d + (error_d * dt)
#			output_d = Kp_d * error_d + Ki * integral_d + Kd_d * derivative_d
#			x_vel = output_d
#			if(x_vel < 0):
#				x_vel = 0

#			x_vel = math.cos(curr_angle) * w
#			y_vel = math.sin(curr_angle) * w

			print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("x_vel, y_vel: "+ str(x_vel)+", "+ str(y_vel))
			print("")
#			print("y_vel: "+ str(y_vel))
#			print("curr_angle: "+str(math.degrees(curr_angle)))


			vel.linear.x = x_vel
			vel.linear.y = y_vel

			previous_error = error

#			previous_error_d = error_d
#			if (w > threshold):
#				print("w>0")
#				vel.angular.z = w
#				vel.linear.x = x_vel 
#			elif (w < -threshold): 
#				print("w<0")
#				vel.angular.z = w
#				vel.linear.x = x_vel
#			else:
#				print("w==0")
#				vel.angular.z = 0
#				vel.linear.x = 0.3
		velocity_publisher.publish(vel)	
		rate.sleep()

if __name__ == "__main__":
    main()
