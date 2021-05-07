import cv2
import numpy as np
import matplotlib.pyplot as plt


##############
## FUNCTION ##
##############

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=100, color=(255, 0, 0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, center=(x, y), radius=200, color=(255, 255, 255), thickness=5)


cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing', draw_circle)

###############################
## SHOWING IMAGE WITH OPENCV ##
###############################

img = np.zeros((1080, 1920, 3), dtype=np.int8)

while True:
    cv2.imshow("drawing", img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()