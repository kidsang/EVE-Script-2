import cv
import cv2

def getROI(src):
    left = src.cols
    right = 0
    top = scr.rows
    bottom = 0

    # for i in xrange(src.rows):
    #     for j in xrange(scr.cols):
    #         if 

img = cv2.imread('img/test.bmp')
print type(img[0, 0])
# cv2.namedWindow("asdf")
# cv2.imshow("asdf", img)
# cv2.waitKey()