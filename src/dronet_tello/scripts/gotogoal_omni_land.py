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


#take in form of x1,x2,x3,x4
goal_x = sys.argv[1]
goal_y = sys.argv[2]
curr_x = 0
curr_y = 0
curr_angle = 0
threshold = 0.1
publishing = True
kill = False

def process_sysargs():
	global goal_x, goal_y
	goal_x = goal_x.split(",")
	goal_y = goal_y.split(",")
	for i in range(0,len(goal_x)):
		goal_x[i] = float(goal_x[i])
		goal_y[i] = float(goal_y[i])


def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True

def process_user_input(data):
	global kill
	if("cancel" in str(data).lower()):
		kill=True

def main():
	global goal_x, goal_y
	global threshold
	global curr_x, curr_y, curr_angle
	global publishing, kill

	process_sysargs()

	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=1)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", String, process_user_input, queue_size=5)

	#nodemap_file = open(os.path.basename(__file__), "w")
	
	#nodemap_file.write(rig.topic_node('/velocity'))


	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0

	# Defaults: Kp = 0.045; Ki = 0.08; Kd = 0.075
	# Super-slow debug mode: Kp = 0.03; Ki = 0.003; Kd = 0.006
	Kp = 0.41
	Ki = 0.003
	Kd = 0.01
	publishing_count = 0
	hover_count = 0
	goal_counter = 0

	while not rospy.is_shutdown():

		distance_to_goal = math.sqrt((goal_x[goal_counter] - curr_x)**2 + (goal_y[goal_counter] - curr_y)**2)
		print("")
		print("distance to goal: "+ str(distance_to_goal))
		angle_to_goal = math.atan2(goal_y[goal_counter]-curr_y, goal_x[goal_counter]-curr_x) - curr_angle
		if (distance_to_goal < threshold):
			vel.linear.x = 0
			vel.linear.y = 0
			print("GOAL REACHED within threshold: " + str(distance_to_goal))
			state_publisher.publish("GOAL REACHED")
			hover_count += dt
			if(hover_count > 5 and goal_counter == len(goal_x)-1):
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				velocity_publisher.publish(vel)
				velocity_publisher.publish(vel)
				velocity_publisher.publish(vel)
				velocity_publisher.publish(vel)
				velocity_publisher.publish(vel)
				state_publisher.publish("Finished behavior")
			elif(hover_count > 7 and goal_counter == len(goal_x)-1):
				exit()
			elif(hover_count > 5 and goal_counter < len(goal_x)-1):
				#exit_count = 0
				hover_count = 0
				integral = 0
				previous_error = 0
				goal_counter +=1
		elif(kill):
			#send land cmd 5 times then exit
			print("User requested land")
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			state_publisher.publish("User requested land")
			exit_count+= 1
			if(exit_count > 5):
				exit()
		else:
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			vel.linear.x = math.cos(angle_to_goal) * w
			#negative sin due to how Tello interprets roll (right = pos)
			vel.linear.y = -math.sin(angle_to_goal) * w

			previous_error = error

			#print("w: "+str(w))
			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			#print("curr_angle: " + str(curr_angle))
			#print("angle_to_goal: " + str(math.degrees(angle_to_goal)))
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
			state_publisher.publish("GO TO GOAL")
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
			state_publisher.publish("NO VICON DATA; LANDING")

		print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		velocity_publisher.publish(vel)	
		publishing = False
		rate.sleep()

if __name__ == "__main__":
    main()
