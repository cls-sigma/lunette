import time
import cv2
import numpy as np

vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(2)
count=0
while True:
    ret1, frame1=vid1.read()
    ret2, frame2 = vid2.read()
    frame1 = cv2.rotate(frame1, cv2.ROTATE_180)
    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        # if 'q' key-pressed break out
        break

    if key == ord("w"):
        # if 'w' key-pressed save both frameA and frameB at same time
        cv2.imwrite(f"camera/left/{count}.jpg", frame1)
        cv2.imwrite(f"camera/right/{count}.jpg", frame2)
        count+=1
    cv2.imshow("frame1", frame1)
    cv2.imshow("frame2", frame2)
vid1.release()
vid2.release()
cv2.destroyAllWindows()