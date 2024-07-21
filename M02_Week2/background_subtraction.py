import numpy as np
import cv2

# Import and Resize images
ini_bg_img = cv2.imread('static/GreenBackground.png', 1)
ini_bg_img = cv2.resize(ini_bg_img, (678, 381))
print(ini_bg_img.shape)

obj_img = cv2.imread('static/Object.png', 1)
obj_img = cv2.resize(obj_img, (678, 381))
print(obj_img.shape)

new_bg_img = cv2.imread('static/NewBackground.jpg.png', 1)
new_bg_img = cv2.resize(new_bg_img, (678, 381))
print(new_bg_img.shape)
