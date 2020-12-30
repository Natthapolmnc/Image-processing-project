import cv2

duck_img=cv2.imread("ducks.jpg",cv2.IMREAD_GRAYSCALE)

duck_blur7=cv2.blur(duck_img,(7,7))
duck_blur25=cv2.blur(duck_img,(25,25))

cv2.imwrite("duck_blur7.jpg",duck_blur7)
cv2.imwrite("duck_blur25.jpg",duck_blur25)