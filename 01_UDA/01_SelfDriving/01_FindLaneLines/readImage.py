import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.jpg')
ysize = img.shape[0]
xsize = img.shape[1]

# print(type(img), xsize, ysize)

# img:     -   [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]   -
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:     -   [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]   -

color_select = np.copy(img)
region_select = np.copy(img)
line_image = np.copy(img)

red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

color_thresholds = (img[:,:,0] < rgb_threshold[0])\
            | (img[:,:,1] < rgb_threshold[1])\
            | (img[:,:,2] < rgb_threshold[2])
# threshold:     -   [   true, true, true, true, true, true   ]   -
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:     -   [   true, true, true, true, true, true   ]   -

# Mask dark pixels as BLACK
color_select[color_thresholds] = [0 ,0, 0]

left_bottom = [0, 719]
right_bottom = [1279, 719]
apex = [600, 400]

# Fit lines (y=Ax+B) to identify the  3 sided region of interest
# np.polyfit() returns the coefficients [A, B] of the fit
# np.ployfit( (point1[x-axel, point2[x-axel]), (point1[y-axel], point2[y-axel]) , degree of poly)
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
print(XX.shape)
print(img.shape)
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

# Color pixels red which are inside the region of interest
region_select[region_thresholds] = [255, 0, 0]

# Find where image is both colored right and in the region
# [not black region (means white area) & selected region] = red color
line_image[~color_thresholds & region_thresholds] = [255,0,0]

# Display the image
plt.subplot(221)
plt.title('img')
plt.imshow(img)
plt.subplot(222)
plt.title('color_select')
plt.imshow(color_select)
plt.subplot(223)
plt.title('region_select')
plt.imshow(region_select)
plt.subplot(224)
plt.title('line_image')
plt.imshow(line_image)
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw = 4)
plt.show()