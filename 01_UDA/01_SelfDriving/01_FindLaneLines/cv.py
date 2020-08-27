import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = cv2.imread('exit-ramp.jpg')
ysize = img.shape[0]
xsize = img.shape[1]
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

# Mask out of selected region as black
img_region = np.copy(img_gray)*0            # draw a 1D black image
vertices = np.array([[(0, ysize), (450, 290), (490, 290), (xsize, ysize)]], dtype=np.int32)
                                            # select region
cv2.fillPoly(img_region, vertices, 255)     # mask region in 1D black image as white
img_edges_region = np.copy(img_edges)
img_edges_region = cv2.bitwise_and(img_edges, img_region)   # mask edges out of the region as black
# bitwise_and： 只要有一个是黑色，就取黑色的
# bitwise_or： 只要有一个不是黑色，就取不是黑色的

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
threshold = 15
min_line_length = 40
max_line_gap = 20
lines = cv2.HoughLinesP(img_edges_region, rho, theta, threshold, np.array([]),
                                             min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
img_line = np.copy(img)*0
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img_line, (x1, y1), (x2, y2), (0, 255, 0), 10)

# Create a RGB binary image to combine with line image
img_edges_RGB = np.dstack((img_edges, img_edges, img_edges))

# Draw the lines on the edge image
img_edges_line = cv2.addWeighted(img_edges_RGB, 0.8, img_line, 1, 0)

# show image
# cv2.imshow('img_gray', img_gray)
# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_edges', img_edges)
# cv2.imshow('img_edges_region', img_edges_region)
# cv2.imshow('img_line', img_line)
# cv2.imshow('img_edges_line', img_edges_line)
# cv2.waitKey(0)

plt.subplot(221)
plt.title('img')
plt.imshow(img)
plt.subplot(222)
plt.title('img_edges')
plt.imshow(img_edges)
plt.subplot(223)
plt.title('img_edges_region')
plt.imshow(img_edges_region)
plt.subplot(224)
plt.title('img_edges_line')
plt.imshow(img_edges_line)
plt.show()
