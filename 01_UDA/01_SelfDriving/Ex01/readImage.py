import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.jpg')
xsize = img.shape[0]
ysize = img.shape[1]
# print(type(img), xsize, ysize)

# img:     -   [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]   -
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:    |    [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]    |
# img:     -   [   [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b], [r,g,b]   ]   -

color_select = np.copy(img)

red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

thresholds = (img[:,:,0] < rgb_threshold[0]) | (img[:,:,1] < rgb_threshold[1]) | (img[:,:,2] < rgb_threshold[2])
# threshold:     -   [   true, true, true, true, true, true   ]   -
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:    |    [   true, true, true, true, true, true   ]    |
# threshold:     -   [   true, true, true, true, true, true   ]   -
color_select[thresholds] = [0 ,0, 0]

plt.imshow(color_select)
plt.show()
