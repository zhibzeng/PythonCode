# -*- coding: utf-8 -*-
import cv2
##  CV_LOAD_IMAGE_COLOR -- BGR
##  CV_LOAD_IMAGE_GRAYSCALE -- grayscale
##  CV_LOAD_IMAGE_UNCHANGED

image = cv2.imread("imgload.jpg",cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.namedWindow("Image")
cv2.imshow("Image", image)
cv2.waitKey (0)
cv2.destroyAllWindows()
cv2.imwrite('opencv.jpg',image)

# params = list()
# params.append(cv2.cv.CV_IMWRITE_PNG_COMPRESSION)
# params.append(8)
# image = cv2.imread("D:/图片/照片/个人相册/imgload.jpg")
# cv2.imwrite("image_processed.png",image,params)