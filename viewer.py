#!/usr/bin/env python
import os
import sys
import time

import cv2
import matplotlib.pyplot as plt


def main():
    path = sys.argv[1]
    prev_images = []
    while True:
        last_image = sorted(os.listdir(path), key=lambda k: int(k.split(".")[0]))[-1]
        if len(prev_images) >= 100 and last_image == prev_images[0]:
            break
        prev_images = prev_images[-99:] + [last_image]
        image_path = os.path.join(path, last_image)
        img = cv2.imread(image_path)
        # cv2.imshow("image", img)
        # cv2.destroyAllWindows()
        plt.figure(1)
        plt.clf()
        plt.imshow(img)
        plt.title("Number " + str(last_image))
        plt.pause(0.01)


if __name__ == "__main__":
    main()
