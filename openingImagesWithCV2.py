import cv2

img = cv2.imread("Data/messi5.jpg")

while True:
    cv2.imshow('Hello', img)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cv2.destroyAllWindows()