import cv2
from utils import get_limits
from PIL import Image

green=[0,255,0] #yellow in BGR colorspace
cap= cv2.VideoCapture(0)
while True:
    ret, frame= cap.read()
    hsvImage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit= get_limits(color=green)

    mask=cv2.inRange(hsvImage,lowerLimit, upperLimit )

    mask_= Image.fromarray(mask)

    bbox= mask_.getbbox()

    if bbox is not None:
        x1 ,y1,x2,y2= bbox

        frame=cv2.rectangle(frame,(x1,y1),(x2,y2), (255,0,0),5) #frame, cooridnates, color of box and thickness of box

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

    