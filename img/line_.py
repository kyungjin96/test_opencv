import cv2
import numpy as np

img_forward = cv2.imread('./img/forward.png',cv2.IMREAD_GRAYSCALE)




rect_img = cv2.rectangle(img_forward,(220,720),(285,780),(255,0,255),3)
rect_img = cv2.rectangle(img_forward,(485,720),(550,780),(255,0,255),3)
rect_img = cv2.rectangle(img_forward,(740,730),(792,792),(255,0,255),3)
rect_img = cv2.rectangle(img_forward,(5,730),(57,792),(255,0,255),3)

left_img = img_forward[720:780,220:285]
right_img = img_forward[720:780,485:550]
rr_img = img_forward[730:792,740:792]
ll_img = img_forward[730:792,5:57]
import numpy as np


if np.all(left_img > 90) and np.all(right_img > 90):
    print('T')

if  np.all(left_img > 90)  :
    print('left')

if  np.all(right_img > 85) :
    print('right')

cv2.imshow('d',img_forward)
cv2.waitKey(0)
cv2.destroyAllWindows()