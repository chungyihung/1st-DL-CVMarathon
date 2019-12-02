#!/usr/bin/python3
import cv2

LENA_IMG_PATH = 'lena.png'
img = cv2.imread(LENA_IMG_PATH, cv2.IMREAD_COLOR)

imgHeight = img.shape[0]
imgWidth = img.shape[1]
imgChannel = img.shape[2]

img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_lab =  cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
resizeFac = 0.4
wndIdx = 1

wndTitle = "HLS"
cv2.namedWindow(wndTitle, cv2.WINDOW_NORMAL)
cv2.imshow(wndTitle, img_hls)
cv2.resizeWindow(wndTitle, (int(imgWidth * resizeFac), int(imgHeight * resizeFac)))
cv2.moveWindow(wndTitle, int(imgWidth * wndIdx * resizeFac), 0)

wndIdx = wndIdx +1

wndTitle = "LAB"
cv2.namedWindow(wndTitle, cv2.WINDOW_NORMAL)
cv2.imshow(wndTitle, img_lab)
cv2.resizeWindow(wndTitle, (int(imgWidth * resizeFac), int(imgHeight * resizeFac)))
cv2.moveWindow(wndTitle, int(imgWidth * wndIdx * resizeFac), 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
