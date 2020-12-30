import cv2 as cv
import numpy as np
from scipy.signal import convolve2d as conv2
from skimage import data, img_as_float
from skimage import color, data, restoration, io
from skimage import exposure
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

img = cv.imread('noise2.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag_spec = 20*np.log(np.abs(fshift))

def blpf(spec_img,D0):
    X=len(spec_img[0])
    Y=len(spec_img)
    nw_img=[]
    for y in tqdm(range(len(spec_img))):
        nw_img.append([])
        for x in range(len(spec_img[0])):
            nw_img[y].append(0)

    for y in tqdm(range(len(spec_img))):
        for x in range(len(spec_img[0])):
            D=((x-(X/2))**2+(y-(Y/2))**(2))**0.5
            butter=1/(1+(D/D0)**2)
            nw_img[y][x]=spec_img[y][x]*butter
    return nw_img

res=blpf(fshift,16)

def idft(img):
    f_ishift = np.fft.ifftshift(img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)
    return img_back


res=idft(res)
cv.imwrite("noise2_unpatt.jpg",res)
img=cv.imread("noise2_unpatt.jpg",0)
res=cv.equalizeHist(img)

cv.imwrite("noise2_clean.jpg",res)

# psf = np.ones((5, 5)) / 25
# img=io.imread("noise3_unpatt.jpg")
# img = color.rgb2gray(img)
# img = conv2(img, psf, 'same')
# img += 0. * img.std() * np.random.standard_normal(img.shape)

# deconvolved, _ = restoration.unsupervised_wiener(img, psf)

# io.imsave("noise3_unpatt.jpg",deconvolved)