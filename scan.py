from transform import four_point_transform
import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# load the image and compute the ratio of the old height
# to the new height, clone it, and resize it
image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)
 
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)        # To make edge detection better
edged = cv2.Canny(gray, 75, 200)
 


# If you are using openCV version below 3, change the first argument to (cnts, _) . The findContours returns 2 args in openCV < 3.0
(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
 
# loop over the contours
for c in cnts:
    # approximate the contour
    perimeter = cv2.arcLength(c, True)
    est = cv2.approxPolyDP(c, 0.02 * perimeter, True)

    # ASSUMPTION : image has 4 vertices
    if len(est) == 4:
        screenCnt = est 
        break
    else :
        screenCnt = 0


newImg = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
 

newImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
newImg = threshold_adaptive(newImg, 251, offset = 10)
newImg = newImg.astype("uint8") * 255
 
# show the original and scanned images

cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(newImg, height = 650))
cv2.waitKey(0)
