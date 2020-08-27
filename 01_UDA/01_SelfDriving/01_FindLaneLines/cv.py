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
# to show the edges in the image
low_threshold = 50
high_threshold = 150
img_edges = cv2.Canny(img_blur, low_threshold, high_threshold)

# Hough space(input image,
#               rho: distance resolution,
#               theta: angular resolution,
#               threshold: number of votes ,
#               np.array([]): empty np.array([]) is just a placeholder,
#               minimum length of a line (in pixels),
#               maximum distance between segments that you will allow to be
#                   connected into a single line)
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 50
max_line_gap = 10
lines = cv2.HoughLinesP(img_edges, rho, theta, threshold, np.array([]),
                                             min_line_length, max_line_gap)
img_line = np.copy(img)*0
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img_line, (x1, y1), (x2, y2), (0, 255, 0), 2)

# show image
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_edges', img_edges)
cv2.imshow('img_line', img_line)
cv2.waitKey(0)