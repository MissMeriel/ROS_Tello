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

#import libh264decoder

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from tellopy import build_packet, TelloCommand

#decoder = libh264decoder.H264Decoder()

def stream_video(output_stream, shutdown_signal):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(.5)
    addrVideo = ('', 6037)
    #addrVideo = ('', 11111)
    sock.bind(addrVideo)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #s.settimeout(1)
    addr = ("192.168.10.1", 8889)
    if(sock is None):
	print("Could not connect to local video socket")
    if(s is None):
	print("Could not connect to Tello video socket")
    print("CONNECTING TO CAMERA...")
    bytes_sent = s.sendto(bytearray(b"conn_req:" + struct.pack("<H", 6037)), addr)
    print("bytes sent: "+str(bytes_sent))
    #s.sendto(bytearray(b"conn_req:" + struct.pack("<H", 11111)), addr)
    #time.sleep(2.0)
    #print("TAKING OFF...")
    #s.sendto(build_packet(TelloCommand.TAKEOFF, sequence_id=1), addr)
    print("REQUESTING VIDEO...")
    bytes_sent = s.sendto(build_packet(TelloCommand.REQ_VIDEO_SPS_PPS, sequence_id=1), addr)
    print("bytes sent: "+str(bytes_sent))
    #s.sendto(b'command', addr)
    #print ('sent: command')
    #s.sendto(b'streamon', addr)
    #print ('sent: streamon')
    #s.close()

    # with open("debug.h264", "w+") as capture_file:
    #     pass

    is_started = False
    packet_data = ""
    timeout_count = 0
    while not shutdown_signal.is_set():
        try:
                res_string = sock.recv(4096)
		data = bytearray(res_string)
        except socket.timeout as e:
	    timeout_count += 1
            print(e)
	    if(timeout_count > 5):
	    	print("REQUESTING VIDEO...")
	    	bytes_sent = s.sendto(build_packet(TelloCommand.REQ_VIDEO_SPS_PPS, sequence_id=1), addr)
            continue
        except socket.error as e:
            print(e)
            break
	timeout_count = 0
        if len(data) > 6 and data[2:6] == b"\x00\x00\x00\x01" and data[6] & 0x1f == 7:
            # sequence parameter set has been received, we can start saving
        	is_started = True
        if is_started:
            # with open("debug.h264", "ab") as capture_file:
            #     capture_file.write(data[2:])
	    print("writing to output_stream...")
            output_stream.write(data[2:])
	print("is_started: "+str(is_started))
	#print("data[2:6] == b\"\x00\x00\x00\x01\": "+str(data[2:6] == b"\x00\x00\x00\x01"))
	#print(data[2:6])
	#print("data[6] & 0x1f == 7: "+str(data[6] & 0x1f == 7))
	print
    sock.close()
    s.close()

def decode_bmp_image(input_stream, shutdown_signal):
    print("in decode_bmp_image")
    camera_raw = rospy.Publisher("image_raw", Image, queue_size=10)
    cnt = 0
    rootpath = "capture"
    if not os.path.exists(rootpath):
        os.makedirs(rootpath)
    while not shutdown_signal.is_set():
	print("reading from input stream...")
        file_size_bytes = bytearray(input_stream.read(6))
        print("IMAGE PROCESSED!")
        print(" size: %s" % file_size_bytes)
        file_size = 0
        for i in range(4):
            file_size += file_size_bytes[i + 2] * 256 ** i
        data = file_size_bytes + input_stream.read(file_size - 6)
        image = cv2.imdecode(np.fromstring(bytes(data), dtype=np.uint8), 1)
        temp = rospy.Time.now()
        cv2.imwrite("{}/{}.jpg".format(rootpath, temp), image)
        print(" decoded!")
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
    print(sys.version)
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
