#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped

goal_x = 1
goal_y = 1
curr_x = 0
curr_y = 0
curr_angle = 0
threshold = 0.18
publishing = True

def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	#curr_angle = data.transform.rotation.z
	# convert quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	global publishing
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	p_publisher = rospy.Publisher("/p", String, queue_size=10)
	i_publisher = rospy.Publisher("/i", String, queue_size=10)
	d_publisher = rospy.Publisher("/d", String, queue_size=10)
	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	Kp = 0.03 
	Ki = 0.003
	Kd = 0.006
	publishing_count = 0

	while not rospy.is_shutdown():

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		print("")		
		print("distance to goal: "+ str(distance_to_goal))
		angle_to_goal = math.atan2(goal_y, goal_x) - curr_angle
		print("angle_to_goal: "+ str(angle_to_goal))
		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			print("")
			state_publisher.publish("Goal reached within threshold: " + str(distance_to_goal))
		else:
			error = distance_to_goal
			error = error * math.sin(angle_to_goal)
			derivative = (error - previous_error) / dt
			p_publisher.publish(str(Kp*error))
			i_publisher.publish(str(Ki*integral))
			d_publisher.publish(str(Kd*derivative))
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			vel.linear.x = math.cos(angle_to_goal) * w
			vel.linear.y = -math.sin(angle_to_goal) * w

			previous_error = error

			print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("curr_angle: " + str(curr_angle))
			print("angle_to_goal: " + str(angle_to_goal))
			print("actual vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
			
			# max tello speed is +-1
			if(vel.linear.y > 1):
				vel.linear.y = 1
			if(vel.linear.y < -1):
				vel.linear.y = -1
			if(vel.linear.x > 1):
				vel.linear.x = 1
			if(vel.linear.x < -1):
				vel.linear.x = -1


		#check that we haven't gone too long without vicon data
		if(not publishing):
			publishing_count += 1
		else:
			publishing_count = 0
		if(publishing_count > 4):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			print("NO VICON DATA; LANDING")

		print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		velocity_publisher.publish(vel)	
		publishing = False
		rate.sleep()

if __name__ == "__main__":
    main()
