import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

ret,frame = cap.read()


while True:
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break