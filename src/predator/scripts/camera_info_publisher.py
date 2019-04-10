#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time
import numpy as np
import std_msgs.msg
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from dronet_tello.msg import FlightData
from dronet_tello.msg import HeadedBool 
import rosgraph.impl.graph as rig
import rospy
import sys, os
from sensor_msgs.msg import CameraInfo

def main():
	rospy.init_node("camera_info", anonymous=True)
	dt = 1.0/20.0
	rate = rospy.Rate(dt)
	camera_info_publisher = rospy.Publisher("/camera_info", CameraInfo, queue_size=1)
	msg = CameraInfo()
	msg.height = rospy.get_param("image_height")
	msg.width =  rospy.get_param("image_width")
	msg.distortion_model = rospy.get_param("distortion_model")
	#print("rospy.get_param(/distortion_coefficients/data) type: "+str(type(rospy.get_param("/distortion_coefficients/data"))))
	D = np.array(rospy.get_param("/distortion_coefficients/data"))
	msg.D = D.tolist()
	msg.K = rospy.get_param("/camera_matrix/data")
	msg.R = rospy.get_param("/rectification_matrix/data")
	msg.P = rospy.get_param("/projection_matrix/data")
	msg.binning_x = 0 # rospy.get_param("")
	msg.binning_y = 0 # rospy.get_param("")
	msg.roi.x_offset = 0 # rospy.get_param("")
	msg.roi.y_offset = 0 # rospy.get_param("")
	msg.roi.height = 0 # rospy.get_param("")
	msg.roi.width = 0 # rospy.get_param("")
	msg.roi.do_rectify = 0 # rospy.get_param("")

	while not rospy.is_shutdown():
		h = std_msgs.msg.Header()
		h.stamp = rospy.Time.now()
		msg.header = h
		camera_info_publisher.publish(msg)


if __name__== "__main__":
	main()

'''
[sensor_msgs/CameraInfo]:
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
uint32 height
uint32 width
string distortion_model
float64[] D
float64[9] K
float64[9] R
float64[12] P
uint32 
uint32 binning_y
sensor_msgs/RegionOfInterest roi
  uint32 x_offset
  uint32 y_offset
  uint32 height
  uint32 width
  bool do_rectify
 
'''
