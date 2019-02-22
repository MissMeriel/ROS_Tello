#!/usr/bin/env python
import Queue
import rospy
import sys
import termios
import threading
import time
import traceback
import tty

from geometry_msgs.msg import Twist

velocity_message = None

def user_velocity_callback(data):
	global velocity_message
	velocity_message = data

def main():
    global velocity_message
    rospy.init_node("key_vel_middleman", anonymous=True)
    velocity_subscriber = rospy.Subscriber("/user_velocity", Twist, user_velocity_callback, queue_size=10)
    velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        velocity_publisher.publish(velocity_message)
        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, ORIG_SETTINGS)

