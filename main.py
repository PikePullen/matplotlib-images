import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
im = Image.open('Mando10.jpg')
print(type(im))

"""images are represented in computers as arrays"""
pic_arr = np.array(im)
# print(arr)
# represents width and height of image, the third value is the pixel color
print(pic_arr.shape)

"""Display the image"""
# plt.imshow(pic_arr)
# plt.show()

""" 
this gets all the values in the x,y,1st index channel
[:,:,1-3]
the first two colon paramters represent the x, y parameters of the image dimensions
the third paramter references the color channel
"""
# red channel values
pic_red = pic_arr.copy()
# pic_red = pic_red[:,:,1]
# plt.imshow(pic_red, cmap='gray')
# plt.show()

# green channel values
pic_green = pic_arr.copy()
pic_green = pic_green[:,:,2]
# plt.imshow(pic_green, cmap='gray')
# plt.show()

# blue channel values
pic_blue = pic_arr.copy()
pic_blue = pic_blue[:,:,2]
# plt.imshow(pic_blue, cmap='gray')
# plt.show()

# Set everything in green channel to zero
pic_red[:,:,1] = 0
# plt.imshow(pic_red, cmap='gray')
# plt.show()

# Set everything in green channel to zero
pic_red[:,:,2] = 0

plt.imshow(pic_red, cmap='gray')
plt.show()
print(pic_red.shape)