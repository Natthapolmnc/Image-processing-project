import numpy as np
import cv2

img=cv2.imread("lotus_gray.jpg",0)

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8))

eight_bit_img = (np.array([int(i[0])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7])*255 for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])         

finalr = cv2.hconcat([eight_bit_img,seven_bit_img,six_bit_img,five_bit_img])
finalv =cv2.hconcat([four_bit_img,three_bit_img,two_bit_img,one_bit_img])
 
final = cv2.vconcat([finalr,finalv])

cv2.imwrite("plane.jpg",final)