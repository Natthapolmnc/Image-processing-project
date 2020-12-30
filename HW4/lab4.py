import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

filename="dog"

img = cv.imread(filename+".jpg",0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


def ilpf(spec_img,D0):
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
            if (D>D0):
                nw_img[y][x]=spec_img[y][x]*0
            if (D<D0):
                nw_img[y][x]=spec_img[y][x]*1
    return nw_img

def ihpf(spec_img,D0):
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
            if (D>D0):
                nw_img[y][x]=spec_img[y][x]*1
            if (D<D0):
                nw_img[y][x]=spec_img[y][x]*0
    return nw_img

def glpf(spec_img,D0):
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
            gauss=math.exp((-1*D**2)/(2*D0))
            nw_img[y][x]=spec_img[y][x]*gauss
    return nw_img

def ghpf(spec_img,D0):
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
            gauss=1-math.exp((-1*D**2)/(2*D0))
            nw_img[y][x]=spec_img[y][x]*gauss
    return nw_img

def bhpf(spec_img,D0):
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
            if (D!=0):
                butter=1/(1+(D0/D)**2)
            if (D==0):
                butter=0
            nw_img[y][x]=spec_img[y][x]*butter
    return nw_img



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

def idft(img):
    f_ishift = np.fft.ifftshift(img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)
    return img_back


q_dict={0:5,1:50,2:150}

res=None
for i in range(3):
    res=ihpf(fshift,q_dict[i])
    res=idft(res)

    plt.subplot(121),plt.imshow(img, cmap= 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(res, cmap = 'gray')
    plt.title('Result'), plt.xticks([]), plt.yticks([])
    plt.savefig("ihpf_"+filename+"_"+"_"+str(q_dict[i])+".jpg")

