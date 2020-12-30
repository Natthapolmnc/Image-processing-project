import cv2
import matplotlib.pyplot as plt

chess1_img=cv2.imread("chess1.jpg",cv2.IMREAD_GRAYSCALE)
chess2_img=cv2.imread("chess2.jpg",cv2.IMREAD_GRAYSCALE)

chess1_blur_img=cv2.blur(cv2.imread("chess1.jpg",cv2.IMREAD_GRAYSCALE),(3,3))
chess2_blur_img=cv2.blur(cv2.imread("chess2.jpg",cv2.IMREAD_GRAYSCALE),(3,3))

chess1_blur11_img=cv2.blur(cv2.imread("chess1.jpg",cv2.IMREAD_GRAYSCALE),(11,11))
chess2_blur11_img=cv2.blur(cv2.imread("chess2.jpg",cv2.IMREAD_GRAYSCALE),(11,11))

chess1_hist=[]
for i in chess1_img:
    for j in i:
        chess1_hist+=[j]

chess2_hist=[]
for i in chess2_img:
    for j in i:
        chess2_hist+=[j]
    


fig, axs = plt.subplots(3, 2, sharey=True, tight_layout=True)

axs[0,0].hist(chess1_hist,bins=256)
axs[0,0].set_title("Original Chess1")
axs[0,1].hist(chess2_hist,bins=256)
axs[0,1].set_title("Original Chess2")

axs[1,0].hist(chess1_blur_img.flatten(),bins=256)
axs[1,0].set_title("3x3 Blur Chess1")
axs[1,1].hist(chess2_blur_img.flatten(),bins=256)
axs[1,1].set_title("3x3 Blur Chess2")

axs[2,0].hist(chess1_blur11_img.flatten(),bins=256)
axs[2,0].set_title("11x11 Blur Chess1")
axs[2,1].hist(chess2_blur11_img.flatten(),bins=256)
axs[2,1].set_title("11x11 Blur Chess2")

plt.savefig("histogram.png")

cv2.imwrite("chess1_blur3.jpg",chess1_blur_img)
cv2.imwrite("chess2_blur3.jpg",chess2_blur_img)

cv2.imwrite("chess1_blur11.jpg",chess1_blur11_img)
cv2.imwrite("chess2_blur11.jpg",chess2_blur11_img)

plt.show()
