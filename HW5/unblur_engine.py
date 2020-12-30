import cv2 as cv
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import color, data, restoration, io
from scipy.signal import convolve2d as conv2
from skimage import data, img_as_float
from skimage import exposure

psf = np.ones((3,3)) / 9
img=io.imread("blurred_happy.jpg")
img = color.rgb2gray(img)
img = conv2(img, psf, 'same')
img += 0.5 * img.std() * np.random.standard_normal(img.shape)

deconvolved, _ = restoration.unsupervised_wiener(img, psf)


io.imsave("unblurred_happy.jpg",deconvolved)

img=io.imread("unblurred_happy.jpg")
deconvolved=cv.medianBlur(img,5)
for kuyuwer in range(1000):
    deconvolved=cv.medianBlur(deconvolved,5)


io.imsave("unblurred_happy.jpg",deconvolved)
# img=cv.imread("unblurred_happy.jpg",0)

# for i in range(len(img)):
#     for j in range(len(img[0])):
#         if (img[i][j]!=255):
#             img[i][j]=img[i][j]-50


# # res=cv.equalizeHist(img)

# cv.imwrite("unblurred_happy.jpg",img)