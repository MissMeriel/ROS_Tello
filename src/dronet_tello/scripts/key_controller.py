import sys
import termios
import time
import traceback
import tty

from tellopy import Tello

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


def main():
    tello = Tello()
    in_air = False
    for key_press in key_presses():
        # sys.stdout.write(",0x%06x" % key_press)
        tello.pitch, tello.roll, tello.yaw, tello.throttle = 0., 0., 0., 0.
        if key_press == Key.SPACE and not in_air:
            tello.take_off()
            in_air = True
        elif key_press == Key.SPACE and in_air:
            tello.land()
            in_air = False
        elif key_press == Key.UP:
            tello.pitch = 1.0
        elif key_press == Key.DOWN:
            tello.pitch = -1.0
        elif key_press == Key.RIGHT:
            tello.roll = 1.0
        elif key_press == Key.LEFT:
            tello.roll = -1.0
        elif key_press == Key.W:
            tello.throttle = 1.0
        elif key_press == Key.S:
            tello.throttle = -1.0
        elif key_press == Key.A:
            tello.yaw = -1.0
        elif key_press == Key.D:
            tello.yaw = 1.0
    tello.shutdown()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, ORIG_SETTINGS)

