#!/usr/bin/python3
import cv2

LENA_IMG_PATH = 'lena.png'
img = cv2.imread(LENA_IMG_PATH, cv2.IMREAD_COLOR)

imgHeight = img.shape[0]
imgWidth = img.shape[1]
imgChannel = img.shape[2]

resizeFac = 0.4

for channel in range(imgChannel):
    wndTitle = "Channel: " + str(channel)
    cv2.namedWindow(wndTitle, cv2.WINDOW_NORMAL)
    cv2.imshow(wndTitle, img[:, :, channel])
    cv2.resizeWindow(wndTitle, (int(imgWidth * resizeFac), int(imgHeight * resizeFac)))
    cv2.moveWindow(wndTitle, int(imgWidth * channel * resizeFac), 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
