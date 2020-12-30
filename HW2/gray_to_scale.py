import cv2

def to_bin(num):
    return bin(num)[2:]

lotus_img=cv2.imread("lotus.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("lotus_gray.jpg",lotus_img)
