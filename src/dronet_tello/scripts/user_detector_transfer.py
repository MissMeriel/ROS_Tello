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


######################################################
# DETERMINES IF USER'S FACE IS POINTED TOWARDS DRONE
######################################################


drone_x = 0
drone_y = 0
user1_x = 0
user1_y = 0
user1_angle = 0
user2_x = 0
user2_y = 0
user2_angle = 0


def vicon_user1(data):
	global user1_x, user1_y, user1_angle
	user1_x = data.transform.translation.x
	user1_y = data.transform.translation.y
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	user1_angle = math.atan2(siny_cosp, cosy_cosp);


def vicon_user2(data):
	global user2_x, user2_y, user2_angle
	user2_x = data.transform.translation.x
	user2_y = data.transform.translation.y
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	user2_angle = math.atan2(siny_cosp, cosy_cosp);


def vicon_drone(data):
	global drone_x, drone_y
	drone_x = data.transform.translation.x
	drone_y = data.transform.translation.y


def is_user1_watching_drone():
	global user1_x, user1_y, user1_angle
	global drone_x, drone_y
	if(abs(math.atan2(user1_y - drone_y, user1_x - drone_x) - user1_angle) < 0.5 ):
		return True
	else:
		return False


def is_user2_watching_drone():
	global user2_x, user2_y, user2_angle
	global drone_x, drone_y
	if(abs(math.atan2(user2_y - drone_y, user2_x - drone_x) - user2_angle) < 0.5 ):
		return True
	else:
		return False


def main():

	rospy.init_node("user_detector", anonymous=True)
	user1_publisher = rospy.Publisher("/is_user1_watching_drone", Bool, queue_size=1)
	user2_publisher = rospy.Publisher("/is_user2_watching_drone", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_drone, queue_size=10)
	user1_subscriber = rospy.Subscriber("/vicon/PLAYER1/PLAYER1", TransformStamped, vicon_user1, queue_size=10)
	user2_subscriber = rospy.Subscriber("/vicon/PLAYER2/PLAYER2", TransformStamped, vicon_user2, queue_size=10)
	
	set_rate = 20
	rate = rospy.Rate(set_rate)

	while not rospy.is_shutdown():
		user1_publisher.publish(is_user1_watching_drone())
		user2_publisher.publish(is_user2_watching_drone())
		rate.sleep()



if __name__ == "__main__":
    main()
