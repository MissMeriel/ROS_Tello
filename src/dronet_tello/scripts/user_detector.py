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
user_x = 0
user_y = 0
user_angle = 0


def vicon_user(data):
	global user_x, user_y, user_angle
	user_x = data.transform.translation.x
	user_y = data.transform.translation.y
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	user_angle = math.atan2(siny_cosp, cosy_cosp);


def vicon_drone(data):
	global drone_x, drone_y
	drone_x = data.transform.translation.x
	drone_y = data.transform.translation.y


def is_user_watching_drone():
	global user_x, user_y, user_angle
	global drone_x, drone_y
	if(abs(math.atan2(user_y - drone_y, user_x - drone_x) - user_angle) < 0.5 ):
		return True
	else:
		return False

def main():

	rospy.init_node("user_detector", anonymous=True)
	user_publisher = rospy.Publisher("/is_user_watching_drone", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_drone, queue_size=10)
	user_subscriber = rospy.Subscriber("vicon/PLAYER1/PLAYER1", TransformStamped, vicon_user, queue_size=10)
	
	set_rate = 20
	rate = rospy.Rate(set_rate)

	while not rospy.is_shutdown():
		user_publisher.publish(is_user_watching_drone())
		rate.sleep()



if __name__ == "__main__":
    main()
