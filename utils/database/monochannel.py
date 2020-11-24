#!/usr/bin/env python3

import cv2
import os
import sys
import shutil


folder_dir = "VM_Database_1k/test/NIR/"
for folder_name in os.listdir(folder_dir):
    lr_count = 0
    print(folder_name)
    for img_name in os.listdir(folder_dir + folder_name):
        image_dir = folder_dir + folder_name + "/" + img_name
        if(img_name[0:2] == 'HR'):
            print("HR!")
            hr_img = cv2.imread(image_dir)
            gray_hr = cv2.cvtColor(hr_img, cv2.COLOR_BGR2GRAY)
            gray_hr = (gray_hr*256).astype('uint16')
            cv2.imwrite(image_dir,gray_hr)
            print(image_dir)  
        elif(img_name[0:2] == 'LR'):
            print("LR!")
            lr_img = cv2.imread(image_dir)
            gray_lr = cv2.cvtColor(lr_img, cv2.COLOR_BGR2GRAY)
            gray_lr = (gray_lr*256).astype('uint16')
            cv2.imwrite(image_dir, gray_lr)
            print(image_dir)    
            lr_count = lr_count + 1
        elif(img_name[0:2] == 'SM'):
            print("SM!")
            sm_img = cv2.imread(image_dir)
            gray_sm = cv2.cvtColor(sm_img, cv2.COLOR_BGR2GRAY)
            gray_sm = (gray_sm*256).astype('uint16')
            cv2.imwrite(image_dir,gray_sm)
            print(image_dir) 

