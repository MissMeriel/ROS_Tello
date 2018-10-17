import time

import tellopy


def main():
    tello = tellopy.Tello()
    print('Taking off')
    tello.take_off()
    time.sleep(5)
    tello.throttle = 0.01
    # tello.pitch = -0.5
    tello.yaw = 1.0
    time.sleep(0.5)
    print('Landing')
    tello.land()
    time.sleep(3)
    print('Shutting down')
    tello.shutdown()


if __name__ == "__main__":
    main()
