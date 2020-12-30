import cv2

fruit_img=cv2.imread("fruit.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imwrite("fruit_gray.jpg",fruit_img)

flower=cv2.imread("flower2.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imwrite("flower_gray.jpg",flower)
