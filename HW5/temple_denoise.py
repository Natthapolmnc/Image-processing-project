import cv2 as cv
import numpy as np
import math
from scipy.signal.signaltools import wiener
from matplotlib import pyplot as plt
from tqdm import tqdm

import numpy as np

def padding(img,pad):

    padded_img = np.zeros((img.shape[0]+2*pad,img.shape[1]+2*pad))
    padded_img[pad:-pad,pad:-pad] = img
    return padded_img

def AdaptiveMedianFilter(img,s=3,sMax=7):

    if len(img.shape) == 3:
        raise Exception ("Single channel image only")

    H,W = img.shape
    a = sMax//2
    padded_img = padding(img,a)

    f_img = np.zeros(padded_img.shape)

    for i in range(a,H+a+1):
        for j in range(a,W+a+1):
            value = Lvl_A(padded_img,i,j,s,sMax)
            f_img[i,j] = value

    return f_img[a:-a,a:-a] 

def Lvl_A(mat,x,y,s,sMax):

    window = mat[x-(s//2):x+(s//2)+1,y-(s//2):y+(s//2)+1]
    Zmin = np.min(window)
    Zmed = np.median(window)
    Zmax = np.max(window)

    A1 = Zmed - Zmin
    A2 = Zmed - Zmax

    if A1 > 0 and A2 < 0:
        return Lvl_B(window)
    else:
        s += 2 
        if s <= sMax:
            return Lvl_A(mat,x,y,s,sMax)
        else:
             return Zmed

def Lvl_B(window):
    h,w = window.shape
    Zmin = np.min(window)
    Zmed = np.median(window)
    Zmax = np.max(window)

    Zxy = window[h//2,w//2]
    B1 = Zxy - Zmin
    B2 = Zxy - Zmax

    if B1 > 0 and B2 < 0 :
        return Zxy
    else:
        return Zmed

img=cv.imread("noisy_temple.jpg",0)
# img=cv.medianBlur(img,3)
res=AdaptiveMedianFilter(img,3,sMax=7)


cv.imwrite("clear_temple.jpg",img)