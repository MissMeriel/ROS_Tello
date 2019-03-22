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
from dronet_tello.msg import FlightData
from dronet_tello.msg import HeadedBool 
import rosgraph.impl.graph as rig

qr_detected = False


def main():
	global qr_detected

	rospy.init_node("sweep", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=1)
	machine_state_publisher = rospy.Publisher("/machine_state", String, queue_size=10)
	mission_state_publisher = rospy.Publisher("/mission_state", String, queue_size=10)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", String, process_user_input, queue_size=5)
	flight_data_subscriber = rospy.Subscriber("/flight_data", String, process_flight_data, queue_size=5)


if __name__ == "__main__":
    main()
