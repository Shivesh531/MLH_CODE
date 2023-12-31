# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MsAjLrTDb0sLhc-9Ja9m9y2VvBh_r5Ji
"""

!pip install pytesseract
!pip install opencv-python

!sudo apt install tesseract-ocr

import cv2
import matplotlib.pyplot as plt

img1= cv2.imread('img1.png')
img2= cv2.imread('img2.png')

plt.imshow(img1)



plt.imshow(img2)

!pip install pyzbar
!sudo apt-get install zbar-tools

from pyzbar.pyzbar import decode

img= cv2.imread('qrimg1.jpg')
plt.imshow(img)

print(decode(img))

qcd = cv2.QRCodeDetector()

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)

print(retval)
print(points)
print(points.shape)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

cv2.imwrite('qrimg1.jpg', img)
plt.imshow(img)

img2= cv2.imread('qrimg2.png')
plt.imshow(img2)

import numpy as np

qcd2 = cv2.QRCodeDetector()

retval2, decoded_info2, points2, straight_qrcode2 = qcd.detectAndDecodeMulti(img2)
print(retval2)
print(decoded_info2)
print(points2,points2.shape)

cv2.fillPoly(img2, pts= np.int32(points2), color=(0,0,0))
plt.imshow(img2)