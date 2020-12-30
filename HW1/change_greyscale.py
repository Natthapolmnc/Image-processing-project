import cv2
import math

def change_greyscale(k, pic):
    cng=8-k
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            pic[i][j] = ((pic[i][j]//(2**cng))/(2**k))*(255)
    return pic


flower_gray=cv2.imread("flower_gray.jpg")
cv2.imwrite("flower_gray_k1.jpg",change_greyscale(1,flower_gray))
flower_gray=cv2.imread("flower_gray.jpg")
cv2.imwrite("flower_gray_k5.jpg",change_greyscale(5,flower_gray))

fruit_gray=cv2.imread("fruit_gray.jpg")
cv2.imwrite("fruit_gray_k1.jpg",change_greyscale(1,fruit_gray))
fruit_gray=cv2.imread("fruit_gray.jpg")
cv2.imwrite("fruit_gray_k5.jpg",change_greyscale(5,fruit_gray))

