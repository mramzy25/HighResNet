#!/usr/bin/python3 

import cv2 as cv
import numpy as np

image = cv.imread("lro1.jpeg")
image16 = (image * 256).astype('uint16')

image100 = cv.cvtColor(image16, cv.COLOR_BGR2GRAY)
image95 = (image100 * 0.95).astype('uint16')
image90 = (image100 * 0.9).astype('uint16')
image85 = (image100 * 0.85).astype('uint16')

hr11 = image100[6000:6384,0:384]
hr12 = image95[6000:6384,0:384]
hr13 = image90[6000:6384,0:384]
hr14 = image85[6000:6384,0:384]

lro_lr1 = cv.resize(hr11, (128,128), interpolation = cv.INTER_NEAREST)
lro_lr2 = cv.resize(hr11, (128,128), interpolation = cv.INTER_LINEAR)
lro_lr3 = cv.resize(hr11, (128,128), interpolation = cv.INTER_CUBIC)
lro_lr4 = cv.resize(hr11, (128,128), interpolation = cv.INTER_AREA)
lro_lr5 = cv.resize(hr11, (128,128), interpolation = cv.INTER_LANCZOS4)
lro_lr6 = cv.resize(hr12, (128,128), interpolation = cv.INTER_NEAREST)
lro_lr7 = cv.resize(hr12, (128,128), interpolation = cv.INTER_LINEAR)
lro_lr8 = cv.resize(hr12, (128,128), interpolation = cv.INTER_CUBIC)
lro_lr9 = cv.resize(hr12, (128,128), interpolation = cv.INTER_AREA)
lro_lr10 = cv.resize(hr12, (128,128), interpolation = cv.INTER_LANCZOS4)
lro_lr11 = cv.resize(hr13, (128,128), interpolation = cv.INTER_NEAREST)
lro_lr12 = cv.resize(hr13, (128,128), interpolation = cv.INTER_LINEAR)
lro_lr13 = cv.resize(hr13, (128,128), interpolation = cv.INTER_CUBIC)
lro_lr14 = cv.resize(hr13, (128,128), interpolation = cv.INTER_AREA)
lro_lr15 = cv.resize(hr13, (128,128), interpolation = cv.INTER_LANCZOS4)
lro_lr16 = cv.resize(hr14, (128,128), interpolation = cv.INTER_NEAREST)
lro_lr17 = cv.resize(hr14, (128,128), interpolation = cv.INTER_LINEAR)
lro_lr18 = cv.resize(hr14, (128,128), interpolation = cv.INTER_CUBIC)
lro_lr19 = cv.resize(hr14, (128,128), interpolation = cv.INTER_AREA)
lro_lr20 = cv.resize(hr14, (128,128), interpolation = cv.INTER_LANCZOS4)

cv.imwrite("lro5/hr.png", hr11)
cv.imwrite("lro5/lr1.png", lro_lr1)
cv.imwrite("lro5/lr2.png", lro_lr2)
cv.imwrite("lro5/lr3.png", lro_lr3)
cv.imwrite("lro5/lr4.png", lro_lr4)
cv.imwrite("lro5/lr5.png", lro_lr5)
cv.imwrite("lro5/lr6.png", lro_lr6)
cv.imwrite("lro5/lr7.png", lro_lr7)
cv.imwrite("lro5/lr8.png", lro_lr8)
cv.imwrite("lro5/lr9.png", lro_lr9)
cv.imwrite("lro5/lr10.png", lro_lr10)
cv.imwrite("lro5/lr11.png", lro_lr11)
cv.imwrite("lro5/lr12.png", lro_lr12)
cv.imwrite("lro5/lr13.png", lro_lr13)
cv.imwrite("lro5/lr14.png", lro_lr14)
cv.imwrite("lro5/lr15.png", lro_lr15)
cv.imwrite("lro5/lr16.png", lro_lr16)
cv.imwrite("lro5/lr17.png", lro_lr17)
cv.imwrite("lro5/lr18.png", lro_lr18)
cv.imwrite("lro5/lr19.png", lro_lr19)
cv.imwrite("lro5/lr20.png", lro_lr20)

#cv.waitKey(0)