import cv2
import numpy as np 


img = cv2.imread('colors.jpg')

rows, cols , _ = img.shape
print('Rows', rows)
print('Cols', cols)



#cut_image 
cut_image = img[100:380 , 0:786] # rows then columns


#Region of Interest
cv2.rectangle(img, (190,370), (535,100), (0,255,0), 3)



cv2.imshow('img', img)
cv2.imshow('Cut img', cut_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


