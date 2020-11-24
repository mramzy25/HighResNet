#!/usr/bin/env python3
import os
import cv2

folder = "VM/train/RED/"
for folder_name in os.listdir(folder):
    it = 0
    for img_name in os.listdir(folder + folder_name):
        image_dir = folder + folder_name + "/" + img_name
        print(image_dir)
        img = cv2.imread(image_dir)

        img16 = (img * 256).astype('uint16')