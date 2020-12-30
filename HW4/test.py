import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt
from tqdm import tqdm



filename="dog"

img = cv.imread(filename+".jpg",0)

f = np.fft.fft2(im g)
fshift = np.fft.fftshift(f)

def idft(img):
    f_ishift = np.fft.ifftshift(img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)
    return img_back

    