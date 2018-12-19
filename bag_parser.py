#!/usr/bin/env python
import argparse
import os

import cv2
import numpy as np
import rosbag
from cv_bridge import CvBridge

from dronet_tello.msg import FlightData

# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import Image

FLIGHT_DATA_ATTRIBUTES = [
    name
    for name in sorted(dir(FlightData))
    if not name.startswith("_") and "serialize" not in name and "header" not in name
]


def flight_data_to_csv(flight_data):
    return ",".join(repr(getattr(flight_data, name)) for name in FLIGHT_DATA_ATTRIBUTES)


def velocity_to_csv(velocity):
    return ",".join(
        [
            repr(velocity.linear.x),
            repr(velocity.linear.y),
            repr(velocity.linear.z),
            repr(velocity.angular.x),
            repr(velocity.angular.y),
            repr(velocity.angular.z),
        ]
    )


def _parse_args():
    parser = argparse.ArgumentParser(description="Bag parser for tello data")
    parser.add_argument("bag_file", type=str, help="The bag file to parse")
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default="./training",
        help="The directory to save data to",
    )
    args = parser.parse_args()
    return args


def main(args):
    path = args.directory
    image_path = os.path.join(path, args.bag_file[:-4])
    data_filename = os.path.join(path, "%s.txt" % args.bag_file[:-4])
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    with open(data_filename, "w+") as data_file:
        data_file.write(
            "image1,image2,{0},{0},{1}\n".format(
                ",".join(FLIGHT_DATA_ATTRIBUTES),
                "linear.x,linear.y,linear.z,angular.x,angular.y,angular.z",
            )
        )
        with rosbag.Bag(args.bag_file) as bag:
            last_2_images = []
            last_2_flight_data = []
            last_message_type = None
            started = False
            for topic, msg, time in bag.read_messages():
                assert len(last_2_images) <= 2
                assert len(last_2_flight_data) <= 2
                if topic == "/image_raw":
                    img = CvBridge().imgmsg_to_cv2(msg, msg.encoding)
                    # img = np.roll(img, 1, axis=-1)
                    image_name = os.path.join(image_path, "{}.jpg".format(time))
                    last_2_images = last_2_images[-1:] + [(image_name, img)]
                    last_message_type = "image"
                elif topic == "/flight_data":
                    last_2_flight_data = last_2_flight_data[-1:] + [msg]
                    last_message_type = "flight_data"
                elif topic == "/velocity":
                    if len(last_2_images) < 2 or len(last_2_flight_data) < 2:
                        print("waiting for data")
                        continue
                    if last_message_type == "velocity":
                        print("multiple velocities for same input")
                        continue
                    if (
                        not started
                        and msg.linear.x == 0.0
                        and msg.linear.y == 0.0
                        and msg.linear.z == 0.0
                        and msg.angular.x == 0.0
                        and msg.angular.y == 0.0
                        and msg.angular.z == 0.0
                    ):
                        print("No movement... waiting for initial command")
                        continue
                    started = True
                    last_2_image_names = []
                    for image_name, img in last_2_images:
                        cv2.imwrite(image_name, img)
                        last_2_image_names.append(image_name)
                    data_file.write(",".join(last_2_image_names))
                    data_file.write(",")
                    data_file.write(
                        ",".join(map(flight_data_to_csv, last_2_flight_data))
                    )
                    data_file.write(",")
                    data_file.write(velocity_to_csv(msg))
                    data_file.write("\n")
                    last_message_type = "velocity"


if __name__ == "__main__":
    main(_parse_args())
