
import cv2
from roboflow import Roboflow
#from vision import ocr1
cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1536)
p="/home/pi/testimage.jpg"

while True:
    ret, image = cam.read()
    image = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imshow('Imagetest',image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        p="/home/pi/testimage.jpg"
        cv2.imwrite(p, image)
        #ocr1(path=p)
        break
  
   
cam.release()
cv2.destroyAllWindows()
