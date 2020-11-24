#!/usr/bin/env python3

import cv2
import os
import sys
import shutil
import numpy as np

folder_dir = "VM/train/RED/"
height = 384
width = 384
blank_img = np.ones((height,width,3), np.uint8)*256
blank_img = (blank_img * 256*256).astype('uint16')


for folder_name in os.listdir(folder_dir):
    cv2.imwrite(folder_dir + folder_name + "/SM.png", blank_img)
    lr_count = 0
    for img_name in os.listdir(folder_dir + folder_name):
        image_dir = folder_dir + folder_name + "/" + img_name
        if(img_name[0:2] == 'HR'):
            print("HR!")
            hr_img = cv2.imread(image_dir)
            hr_img = (hr_img * 256).astype('uint16')
            gray_hr = cv2.cvtColor(hr_img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(folder_dir + folder_name + "/HR.png",gray_hr)
            print(image_dir)  
        elif(img_name[0:2] == 'LR'):
            print("LR!")
            lr_img = cv2.imread(image_dir)
            lr_img = (lr_img * 256).astype('uint16')
            gray_lr = cv2.cvtColor(lr_img, cv2.COLOR_BGR2GRAY)
            if(lr_count < 10):
                cv2.imwrite(folder_dir + folder_name + "/LR00" + str(lr_count) + ".png", gray_lr)
                cv2.imwrite(folder_dir + folder_name + "/QM00" + str(lr_count) +".png", blank_img)
            else:
                cv2.imwrite(folder_dir + folder_name + "/LR0" + str(lr_count) + ".png", gray_lr)
                cv2.imwrite(folder_dir + folder_name + "/QM0" + str(lr_count) +".png", blank_img)
            print(image_dir)    
            lr_count = lr_count + 1
            if (lr_count >= 20):
                break
