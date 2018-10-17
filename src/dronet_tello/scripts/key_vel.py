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

ORIG_SETTINGS = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)


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
    rospy.init_node("key_vel", anonymous=True)
    velocity_publisher = rospy.Publisher("velocity", Twist, queue_size=10)
    linear_vel_x = 0.0
    linear_vel_y = 0.0
    linear_vel_z = 0.0
    angular_vel = 0.0

    q = Queue.Queue()
    kp_thread = threading.Thread(target=key_press_thread, args=(q,))
    kp_thread.start()

    cnt = 0
    sys.stdout.write("Waiting for input...\r\n")
    while kp_thread.is_alive():
        try:
            key_press = q.get(timeout=0.1)
        except Queue.Empty:
            key_press = None

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
        # elif cnt == 5:
        #     cnt = 0
        #     if abs(angular_vel) > 1e-3:
        #         angular_vel -= sign(angular_vel) * 0.1
        #     if linear_vel < -1e-3:
        #         linear_vel -= sign(linear_vel) * 0.1
        #     if linear_vel > 1e-3:
        #         linear_vel -= sign(linear_vel) * 0.1
        # else:
        #     cnt += 1

        velocity = Twist()
        velocity.linear.x = linear_vel_x
        velocity.linear.z = linear_vel_z
        velocity.angular.z = angular_vel
        velocity_publisher.publish(velocity)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, ORIG_SETTINGS)

