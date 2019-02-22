#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import Float64
from std_msgs.msg import String


######################################################
# DETERMINES DRONE'S DISTANCE FROM VARIOUS POINTS
######################################################


drone_x = 0
drone_y = 0
obstacle_x = 0
obstacle_y = 0
user1_x = 0
user1_y = 0
user1_angle = 0
user2_x = 0
user2_y = 0
user2_angle = 0
distance_to_obstacle = None
distance_to_goal = None
distance_to_user1 = None
distance_to_user2 = None

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

def vicon_obstacle(data):
	global obstacle_x, obstacle_y
	obstacle_x = data.transform.translation.x
	obstacle_y = data.transform.translation.y

def distance_to_obstacle():
	global obstacle_x, obstacle_y
	global drone_x, drone_y
	if(obstacle_x!= None and obstacle_y != None and drone_x != None and drone_y != None):
		return math.sqrt(math.pow(obstacle_x - drone_x, 2) + math.pow(obstacle_y - drone_y, 2))	
	else:
		return None

def distance_to_user1():
	global obstacle_x, obstacle_y
	global user1_x, user1_y
	if(obstacle_x!= None and obstacle_y != None and drone_x != None and drone_y != None):
		return math.sqrt(math.pow(user1_x - drone_x, 2) + math.pow(user1_y - drone_y, 2))
	else:
		return None

def distance_to_user2():
	global obstacle_x, obstacle_y
	global user2_x, user2_y
	if(obstacle_x!= None and obstacle_y != None and drone_x != None and drone_y != None):
		return math.sqrt(math.pow(user2_x - drone_x, 2) + math.pow(user2_y - drone_y, 2))
	else:
		return None

def main():

	rospy.init_node("user_detector", anonymous=True)
	obstacle_distance_publisher = rospy.Publisher("/distance_to_obstacle", Float64, queue_size=1)
	user1_distance_publisher = rospy.Publisher("/distance_to_user1", Float64, queue_size=1)
	user2_distance_publisher = rospy.Publisher("/distance_to_user2", Float64, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_drone, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("/vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	user1_subscriber = rospy.Subscriber("vicon/PLAYER1/PLAYER1", TransformStamped, vicon_user1, queue_size=10)
	user2_subscriber = rospy.Subscriber("vicon/PLAYER2/PLAYER2", TransformStamped, vicon_user2, queue_size=10)
	
	set_rate = 20
	rate = rospy.Rate(set_rate)

	while not rospy.is_shutdown():
		obstacle_distance_publisher.publish(distance_to_obstacle())
		user1_distance_publisher.publish(distance_to_user1())
		user2_distance_publisher.publish(distance_to_user2())
		rate.sleep()



if __name__ == "__main__":
    main()
