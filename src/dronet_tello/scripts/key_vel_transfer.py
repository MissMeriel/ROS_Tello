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
from std_msgs.msg import Bool
from std_msgs.msg import String

ORIG_SETTINGS = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)

enabled = False
enabled1 = False
enabled2 = True
obstacle_detected = False
enabled_state = False
gtg = False
kill=False

def key_presses():
    while True:  # ESC
        x = [ord(sys.stdin.read(1))]
        if x == [27]:
            c = [ord(sys.stdin.read(1))]
            if c == [27]:
                break
            elif c == [91]:
                x += c + [ord(sys.stdin.read(1))]
            else:
                x = c
        if x == [3]:
            break
        yield Key.make(x)

def process_user_input(data):
	global enabled1, enabled2, gtg

def process_state(data):
	global gtg, enabled1, enabled2, enabled
	strdata = str(data)
	if("GO TO GOAL" in strdata):
		gtg = True
		enabled = False
	if("Waiting for user input" in strdata):
		enabled=False
		gtg=False
	if("MANUAL1" in strdata):
		enabled1=True
	if("MANUAL2" in strdata):
		enabled2=True

def obstacle_detected(data):
	global obstacle_detected
	obstacle_detected=data

def killswitch(data):
	global kill
	kill=data

class Key:
    SPACE = 0x20

    UP = 0x1b5b41
    DOWN = 0x1b5b42
    RIGHT = 0x1b5b43
    LEFT = 0x1b5b44

    W = 0x57
    A = 0x41
    S = 0x53
    D = 0x44
    X = 0x58

    I = 0x49
    J = 0x4A
    K = 0x4B
    L = 0x4C
    M = 0x4D

    @classmethod
    def make(cls, value):
        if len(value) == 1:
            value = [ord(chr(value[0]).upper())]
        return sum(v * 256 ** (len(value) - i - 1) for i, v in enumerate(value))


def key_press_thread(q):
    for key_press in key_presses():
        q.put(key_press)


def sign(value):
    if value < 0.0:
        return -1.0
    elif value > 0.0:
        return 1.0
    return 0.0


def main():
    global gtg, enabled1, enabled2, kill

    rospy.init_node("key_vel", anonymous=True)
    velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
    input_subscriber = rospy.Subscriber("/obstacle_detector", Bool, obstacle_detected, queue_size=5)
    input_subscriber = rospy.Subscriber("/keys_enabled", Bool, process_user_input, queue_size=5)
    state_subscriber = rospy.Subscriber("/state", String, process_state, queue_size=5)
    process_killer = rospy.Subscriber("/killswitch", Bool, killswitch, queue_size=5)
    user_input_subscriber = rospy.Subscriber("/user_input", String, process_user_input, queue_size=10)
    linear_vel_x = 0.0
    linear_vel_y = 0.0
    linear_vel_z = 0.0
    angular_vel = 0.0
    kill=False
    q = Queue.Queue()
    kp_thread = threading.Thread(target=key_press_thread, args=(q,))
    kp_thread.start()

    cnt = 0
    sys.stdout.write("")
    sys.stdout.write("Waiting for input...\r\n")
    while kp_thread.is_alive():
	if(kill):
		exit()
	try:
	    key_press = q.get(timeout=0.1)
	except Queue.Empty:
	    key_press = None
	#if(enabled1 or obstacle_detected):
	if(enabled1 or obstacle_detected):
		sys.stdout.write("Pressed key: %s, %s\r\n" % (key_press, cnt))
		if key_press == Key.A:
		    angular_vel = min(0.0, max(-1.0, angular_vel - 0.2))
		elif key_press == Key.D:
		    angular_vel = max(0.0, min(1.0, angular_vel + 0.2))
		elif key_press == Key.UP:
		    linear_vel_x = max(0.0, min(1.0, linear_vel_x + 0.2))
		elif key_press == Key.DOWN:
		    linear_vel_x = min(0.0, max(-1.0, linear_vel_x - 0.2))
		elif linear_vel_x < -1e-3:
		    linear_vel_x -= sign(linear_vel_x) * 0.1

		if key_press == Key.S:
		    linear_vel_z = max(-1.0, linear_vel_z - 0.5)
		elif key_press == Key.W:
		    linear_vel_z = min(1.0, linear_vel_z + 0.5)
		if key_press == Key.X:
			linear_vel_x = 0
			linear_vel_y = 0
			linear_vel_z = -200
		if(key_press == Key.J or key_press == Key.K or key_press == Key.L or key_press == Key.I or key_press == Key.M):
			sys.stdout.write("User 2 disabled; User 1 has control")
		velocity = Twist()
		velocity.linear.x = linear_vel_x
		velocity.linear.z = linear_vel_z
		velocity.angular.z = angular_vel
		velocity_publisher.publish(velocity)
	elif(enabled2):
		sys.stdout.write("Pressed key: %s, %s\r\n" % (key_press, cnt))
		if key_press == Key.J:
		    angular_vel = min(0.0, max(-1.0, angular_vel - 0.2))
		elif key_press == Key.L:
		    angular_vel = max(0.0, min(1.0, angular_vel + 0.2))
		elif key_press == Key.UP:
		    linear_vel_x = max(0.0, min(1.0, linear_vel_x + 0.2))
		elif key_press == Key.DOWN:
		    linear_vel_x = min(0.0, max(-1.0, linear_vel_x - 0.2))
		elif linear_vel_x < -1e-3:
		    linear_vel_x -= sign(linear_vel_x) * 0.1

		if key_press == Key.K:
		    linear_vel_z = max(-1.0, linear_vel_z - 0.5)
		elif key_press == Key.I:
		    linear_vel_z = min(1.0, linear_vel_z + 0.5)

		if key_press == Key.X:
			linear_vel_x = 0
			linear_vel_y = 0
			linear_vel_z = -200

		if(key_press == Key.A or key_press == Key.S or key_press == Key.D or key_press == Key.W or key_press == Key.X):
			sys.stdout.write("User 2 disabled; User 1 has control")

		velocity = Twist()
		velocity.linear.x = linear_vel_x
		velocity.linear.z = linear_vel_z
		velocity.angular.z = angular_vel
		velocity_publisher.publish(velocity)
	elif(gtg):
		sys.stdout.write("Key control disabled during go-to-goal.")
	else:
		sys.stdout.write("Key control disabled.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, ORIG_SETTINGS)

