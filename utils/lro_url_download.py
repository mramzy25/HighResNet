#!/usr/bin/env python3
import pandas as pd
import requests
import shutil
import os.path
from os import path


# Read CSV
imageData = pd.read_csv("image_list_Apollo12.csv")
urlSource = imageData[" edr_source"]
imageNames = imageData[" productid"]
missionName = "/media/jota/Elements/Apollo12"

for value in urlSource:
    imageToDownload = requests.get(value, stream = True)

    if imageToDownload.status_code == 200:

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        imageToDownload.raw.decode_content = True
        
        fileToSave = missionName + value[108:]
        print(fileToSave[21:])
        if(fileToSave[21:] != "/media/jota/Elements/Apollo12/"):
            fileToSave = missionName + value[109:]

        # Open a local file with wb ( write binary ) permission.
        with open(fileToSave,'wb') as f:
            shutil.copyfileobj(imageToDownload.raw, f)
        print('Image sucessfully Downloaded: ',fileToSave)

    else:
        print('Image Couldn\'t be retreived')