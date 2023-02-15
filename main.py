import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
im = Image.open('Mando10.jpg')
print(type(im))

"""images are represented in computers as arrays"""
arr = np.array(im)
# print(arr)
# represents width and height of image, the third value is the pixel color
print(arr.shape)

"""Display the image"""
# plt.imshow(arr)
# plt.show()

"""This collapses the color dimension, effectively removing the 3 from earlier"""
# this effectively creates a heatmap image
# gray = arr.mean(axis=2)
# print(gray.shape)
# plt.imshow(gray)
# plt.show()

gray = arr.mean(axis=2)
print(gray.shape)
plt.imshow(gray, cmap='gray')
plt.show()