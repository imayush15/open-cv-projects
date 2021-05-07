import numpy as np
import matplotlib.pyplot as plt
import cv2

# VARIABLES
drawing = False  # True while mouse button down and False while mouse button UP
ix = -1
iy = -1

# FUNCTION
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), thickness=-1, color=(255, 0, 0))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), thickness=-1, color = (255, 0, 0))

# SHOWING THE IMAGE
img = np.zeros((1000, 1000, 3))

cv2.namedWindow(winname='drag')
cv2.setMouseCallback('drag', draw_rectangle)

while True:
    cv2.imshow('drag', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
