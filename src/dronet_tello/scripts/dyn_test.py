#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import Bool
from std_msgs.msg import String
#from vicon_bridge import Marker


goal_x = 1
goal_y = 1
obs_x = -20
obs_y = -20
obs_z = -20
obs_corner_x = 0
obs_corner_y = 0
obs_angle = 0
curr_x = 0
curr_y = 0
#curr_angle: yaw relative to global frame
curr_angle = 0
publishing = True
avoid = False
prev_data = TransformStamped
obstacle_dyn = False
obs_angle_prev = obs_angle


def vicon_obstacle(data):
	global obs_x, obs_y, obs_z, obs_angle, obstacle_dyn, publishing
	x_change = abs(obs_x - data.transform.translation.x) > 0.001
	y_change = abs(obs_y - data.transform.translation.y) > 0.001
	z_change = abs(obs_z - data.transform.translation.z) > 0.001
	rot_change = abs(obs_angle - data.transform.rotation.z) > 0.2
	if(x_change or y_change or z_change or rot_change):
		obstacle_dyn = True
	else:
		obstacle_dyn = False
	print("x_change: "+str(x_change))
	print("y_change: "+str(y_change))
	print("z_change: "+str(z_change))
	print("rot_change: "+str(rot_change))
	print("")
	# quaternions to radians
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle = data.transform.rotation.z
	publishing = True

def obstacle_markers(data):
	#get peripheral points of obstacle and decide which is nearest to current position
	if(data.subject_name == "OBSTACLE"):
		print("OBSTACLE Marker data:")
		print(data.translation)
		print("")

def main():
	global goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid, dynamic_obstacle
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	#obstacle_markers_subscriber = rospy.Subscriber("/vicon/markers", Marker, obstacle_markers, queue_size=10)

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	str_msg = ""

	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	publishing_count = 0
	avoid = False
	final_goal_x = goal_x
	final_goal_y = goal_y
	threshold = 0.1
	obstacle_threshold = 0.275
	angle_threshold = 0.5
	detection_distance = 0.5
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 5
	
	while not rospy.is_shutdown():
		if(obstacle_dyn):
			hover_count -= dt
			print("Transferring control in "+str(int(hover_count))+" seconds")
			str_msg="Transferring control in "+str(int(hover_count))+" seconds"
			if(hover_count <= 0):
				hover_count = 0
				print("KEY VEL enabled")
				str_msg="KEY VEL enabled"
				print("")
		else:
			print("OBSTACLE static")
			str_msg="OBSTACLE static"
			print("")
			hover_count=5

		#check for lapse in vicon data
		if(not publishing):
			publishing = False
			publishing_count += 1
		else:
			publishing_count = 0
			publishing = True
		if(publishing_count > 5):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -500
			print("NO VICON DATA")

		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()



if __name__ == "__main__":
    main()
