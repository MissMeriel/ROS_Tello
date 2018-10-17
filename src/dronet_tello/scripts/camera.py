#!/usr/bin/env python
import os
import socket
import struct
import subprocess as sp
import sys
import threading
import time

import cv2
import imageio
import numpy as np
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from tellopy import build_packet, TelloCommand


def stream_video(output_stream, shutdown_signal):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addrVideo = ("", 6037)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(.5)
    sock.bind(addrVideo)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    addr = ("192.168.10.1", 8889)
    print("CONNECTING TO CAMERA...")
    s.sendto(bytearray(b"conn_req:" + struct.pack("<H", 6037)), addr)
    time.sleep(2.0)
    # print("TAKING OFF...")
    # s.sendto(build_packet(TelloCommand.TAKEOFF, sequence_id=1), addr)
    s.close()

    # with open("debug.h264", "w+") as capture_file:
    #     pass

    is_started = False
    while not shutdown_signal.is_set():
        try:
            data = bytearray(sock.recv(4096))
        except socket.timeout as e:
            continue
        except socket.error as e:
            print(e)
            break
        if len(data) > 6 and data[2:6] == b"\x00\x00\x00\x01" and data[6] & 0x1f == 7:
            # sequence parameter set has been received, we can start saving
            is_started = True
        if is_started:
            # with open("debug.h264", "ab") as capture_file:
            #     capture_file.write(data[2:])
            output_stream.write(data[2:])
    sock.close()


def decode_bmp_image(input_stream, shutdown_signal):
    camera_raw = rospy.Publisher("image_raw", Image, queue_size=10)
    cnt = 0
    rootpath = "capture"
    if not os.path.exists(rootpath):
        os.makedirs(rootpath)
    while not shutdown_signal.is_set():
        file_size_bytes = bytearray(input_stream.read(6))
        # print("IMAGE PROCESSED!")
        # print(" size: %s" % file_size_bytes)
        file_size = 0
        for i in range(4):
            file_size += file_size_bytes[i + 2] * 256 ** i
        data = file_size_bytes + input_stream.read(file_size - 6)
        image = cv2.imdecode(np.fromstring(bytes(data), dtype=np.uint8), 1)
        temp = rospy.Time.now()
        cv2.imwrite("{}/{}.jpg".format(rootpath, temp), image)
        # print(" decoded!")
        # image = np.roll(image, 2, axis=-1)
        image_msg = CvBridge().cv2_to_imgmsg(image)
        image_msg.header.stamp = rospy.Time.now()
        # image_msg.encoding = "RGB8"
        rospy.loginfo("DECODED IMAGE")
        camera_raw.publish(image_msg)
        cnt += 1


def main():
    rospy.init_node("tello_camera_feed", anonymous=True)
    ffmpegCmd = [
        "ffmpeg",
        "-i",
        "-",
        "-f",
        # "rawvideo",
        "h264",
        "-vcodec",
        "bmp",
        # "png",
        "-vf",
        "fps=5",
        # "fps=2",
        "-",
    ]
    print(" ".join(ffmpegCmd))
    with open("ffmpeg.err", "w+") as ffmpeg_err:
        ffmpeg = sp.Popen(ffmpegCmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=ffmpeg_err)

    shutdown_signal = threading.Event()

    decode_thread = threading.Thread(
        target=decode_bmp_image, args=(ffmpeg.stdout, shutdown_signal)
    )
    decode_thread.start()

    time.sleep(0.5)

    stream_thread = threading.Thread(
        target=stream_video, args=(ffmpeg.stdin, shutdown_signal)
    )
    stream_thread.start()

    while not rospy.is_shutdown():
        pass
    shutdown_signal.set()


if __name__ == "__main__":
    main()
