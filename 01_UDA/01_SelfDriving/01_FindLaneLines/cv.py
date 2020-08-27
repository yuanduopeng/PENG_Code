import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = cv2.imread('exit-ramp.jpg')

# cvtColor(input image, convert type)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# GaussianBlur (input image, (ksize, ksize: positive and odd), )
kernel_size = 3
img_blur = cv2.GaussianBlur(img_gray, (kernel_size, kernel_size), 0)

# canny(input image, low, high threshold)
low_threshold = 50
high_threshold = 150
img_edges = cv2.Canny(img_blur, low_threshold, high_threshold)

# show image
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_edges', img_edges)
cv2.waitKey(0) 