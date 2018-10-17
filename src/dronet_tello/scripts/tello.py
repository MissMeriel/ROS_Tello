#!/usr/bin/env python
import time
import rospy
from dronet_tello.msg import FlightData
from geometry_msgs.msg import Twist
from tellopy import Tello

TELLO = Tello()


def velocity_handler(velocity_cmd):
    # rospy.loginfo(
    #     "P: %.3f, R: %.3f, Y: %.3f, T: %.3f",
    #     TELLO.pitch,
    #     TELLO.roll,
    #     TELLO.yaw,
    #     TELLO.throttle,
    # )
    TELLO.pitch = velocity_cmd.linear.x
    TELLO.yaw = velocity_cmd.angular.z
    TELLO.throttle = velocity_cmd.linear.z


def build_msg(flight_data):
    msg = FlightData()
    msg.header.stamp = rospy.Time.now()
    for name, value in sorted(flight_data.__dict__.items()):
        if not name.startswith("_"):
            setattr(msg, name, value)
    return msg


def main():
    rospy.init_node("tello", anonymous=True)
    rospy.loginfo("Taking off.")
    TELLO.take_off()
    time.sleep(5)
    TELLO.throttle = -0.5
    time.sleep(0.5)
    # # time.sleep(0.7)
    # TELLO.throttle = 0.5
    # time.sleep(0.5)
    # TELLO.throttle = -1.0
    # time.sleep(0.4)
    # TELLO.throttle = 0.5
    # time.sleep(2.0)
    # TELLO.throttle = 0.0
    velocity_subscriber = rospy.Subscriber(
        "/velocity", Twist, velocity_handler, queue_size=1
    )
    flight_data_publisher = rospy.Publisher("/flight_data", FlightData, queue_size=1)
    while not rospy.is_shutdown():
        if TELLO.flight_data is not None:
            flight_data_publisher.publish(build_msg(TELLO.flight_data))
    rospy.loginfo("Landing.")
    TELLO.land()
    TELLO.shutdown()


if __name__ == "__main__":
    main()
