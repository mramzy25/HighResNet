#!/usr/bin/env python3

import cv2
import os
import sys
import shutil
from os import path

folder = "VM_Database_1K/8/"
it = 0
it_hr = 0
height = 384
width = 384
'''
for img_name in os.listdir(folder):
    print(img_name)
    image_dir = folder + img_name
    img = cv2.imread(image_dir)
    if img is None:
        sys.exit("Could not read the image.")
    it = 0
    for i in range(5):
        for j in range(10):
            crop = img[i*384:(i+1)*384, j*384:(j+1)*384]
            crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            print(it)
            if it > 9:
                if not(path.exists(folder + "imageset00"+str(it)+"/")):
                    os.mkdir(folder + "imageset00"+str(it)+"/")
                cv2.imwrite(folder + "imageset00"+str(it)+"/"+"HR" + str(it_hr)+ ".png",crop)
            else:
                if not(path.exists(folder + "imageset000"+str(it)+"/")):
                    os.mkdir(folder + "imageset000"+str(it)+"/")
                cv2.imwrite(folder + "imageset000"+str(it)+"/"+"HR" + str(it_hr)+ ".png",crop)
            it = it + 1
            it_hr = it_hr + 1
'''

for folder_name in os.listdir(folder):
    it = 0
    for img_name in os.listdir(folder + folder_name):
        image_dir = folder + folder_name + "/" + img_name
        print(image_dir)
        img = cv2.imread(image_dir)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res1 = cv2.resize(img, (128,128), interpolation = cv2.INTER_NEAREST)
        res2 = cv2.resize(img, (128,128), interpolation = cv2.INTER_LINEAR)
        res3 = cv2.resize(img, (128,128), interpolation = cv2.INTER_CUBIC)
        res4 = cv2.resize(img, (128,128), interpolation = cv2.INTER_AREA)
        res5 = cv2.resize(img, (128,128), interpolation = cv2.INTER_LANCZOS4)
        if it > 9:
            cv2.imwrite(folder + folder_name + "/" + "LR0" + str(it) + ".png", res1)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR0" + str(it) + ".png", res2)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR0" + str(it) + ".png", res3)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR0" + str(it) + ".png", res4)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR0" + str(it) + ".png", res5)
            it = it + 1

        else:
            cv2.imwrite(folder + folder_name + "/" + "LR00" + str(it) + ".png", res1)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR00" + str(it) + ".png", res2)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR00" + str(it) + ".png", res3)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR00" + str(it) + ".png", res4)
            it = it + 1
            cv2.imwrite(folder + folder_name + "/" + "LR00" + str(it) + ".png", res5)
            it = it + 1
        if it == 19:
            break
