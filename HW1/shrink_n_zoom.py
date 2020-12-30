import cv2


# ############# fruit

fruit_gray=cv2.imread("fruit_gray.jpg")

shrink_fruit=cv2.resize(fruit_gray,None,fx=1/6,fy=1/6)

fruit_near_inter=cv2.resize(shrink_fruit,None,fx=6,fy=6,interpolation=cv2.INTER_NEAREST)
cv2.imwrite("fruit_nearest.jpg",fruit_near_inter)

fruit_bilinear=cv2.resize(shrink_fruit,None,fx=6,fy=6,interpolation=cv2.INTER_LINEAR)
cv2.imwrite("fruit_bilinear.jpg",fruit_bilinear)



# ########### FLOWER

flower_gray=cv2.imread("flower_gray.jpg")

shrink_flower=cv2.resize(flower_gray,None,fx=1/6,fy=1/6)

flower_near_inter=cv2.resize(shrink_flower,None,fx=6,fy=6,interpolation=cv2.INTER_NEAREST)
cv2.imwrite("flower_nearest.jpg",flower_near_inter)

flower_bilinear=cv2.resize(shrink_flower,None,fx=6,fy=6,interpolation=cv2.INTER_LINEAR)
cv2.imwrite("flower_bilinear.jpg",flower_bilinear)
