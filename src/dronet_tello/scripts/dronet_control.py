#!/usr/bin/env python
import rospy
from dronet_tello.msg import CNN_out
from geometry_msgs.msg import Twist


class DronetController:
    def __init__(self, alpha_v=0.3, alpha_yaw=0.5, max_forward=0.2, critical_prob=0.7):
        self.velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
        self.predictions_subscriber = rospy.Subscriber(
            "/cnn_out/predictions", CNN_out, self.predicton_handler, queue_size=1
        )

        self.alpha_v = alpha_v
        self.alpha_yaw = alpha_yaw
        self.max_forward = max_forward
        self.critical_prob = critical_prob

        self.rate = rospy.Rate(10)  # rospy.Rate(30)

        self.desired_forward_v = 0.0 # self.max_forward
        self.desired_angular_v = 0.0

        self.steering_angle = 0.0
        self.collision_probability = 1.0

    def predicton_handler(self, msg):
        self.steering_angle = msg.steering_angle
        self.collision_probability = msg.collision_prob

        if self.steering_angle < -1.0:
            self.steering_angle = -1.0
        if self.steering_angle > 1.0:
            self.steering_angle = 1.0

    def run(self):
        while not rospy.is_shutdown():
            # try:
            #     msg = rospy.wait_for_message("/cnn_out/predictions", CNN_out, timeout=5)
            # except:
            #     rospy.logwarn("Controller is not receiving messages")
            #     continue
            # self.steering_angle = msg.steering_angle
            # self.collision_probability = msg.collision_prob
            if self.steering_angle < -1.0:
                self.steering_angle = -1.0
            if self.steering_angle > 1.0:
                self.steering_angle = 1.0
            desired_forward_v_ = (1.0 - self.collision_probability) * self.max_forward
            if desired_forward_v_ <= 0.0:
                rospy.loginfo(
                    "Detected negative forward velocity! Drone will now stop!"
                )
                desired_forward_v_ = 0

            # Low pass filter the velocity and integrate it to get the position
            self.desired_forward_v = (
                1.0 - self.alpha_v
            ) * self.desired_forward_v + self.alpha_v * desired_forward_v_

            rospy.loginfo(
                "Desired_Forward_Velocity [0-1]: %.3f ", self.desired_forward_v
            )

            # Stop if velocity is prob of collision is too high
            if self.desired_forward_v < ((1 - self.critical_prob) * self.max_forward):
                self.desired_forward_v = 0.0

            # Low pass filter the angular_velocity
            self.desired_angular_v = (
                1.0 - self.alpha_yaw
            ) * self.desired_angular_v + self.alpha_yaw * self.steering_angle

            rospy.loginfo(
                "Desired_Angular_Velocity[0-1]: %.3f ", self.desired_angular_v
            )

            # Prepare command velocity
            velocity = Twist()
            velocity.linear.x = self.desired_forward_v
            velocity.angular.z = self.desired_angular_v

            self.velocity_publisher.publish(velocity)

            rospy.loginfo(
                "Collision Prob.: %.3f - OutSteer: %.3f",
                self.collision_probability,
                self.steering_angle,
            )
            rospy.loginfo("--------------------------------------------------")

            self.rate.sleep()


def main():
    rospy.init_node("dronet_control", anonymous=True)
    # works OK
    # controller = DronetController(
    #     alpha_v=0.9, alpha_yaw=0.9, critical_prob=0.85, max_forward=0.35
    # )
    # works better
    # controller = DronetController(
    #     alpha_v=0.99, alpha_yaw=0.9, critical_prob=0.85, max_forward=0.35
    # )
    controller = DronetController(
        alpha_v=0.99, alpha_yaw=0.7, critical_prob=0.9, max_forward=0.35
    )
    controller.run()


if __name__ == "__main__":
    main()
