import base64

import numpy as py
import cv2

capture=cv2.VideoCapture(0)
print(capture.isOpened())
file=open('final.txt','wb')
while(True):
    ret,frame=capture.read()
    if ret==True:
        cv2.namedWindow('senderframe',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('senderframe',frame)
        retval, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        file.write(jpg_as_text)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

file.close()
capture.release()
cv2.destroyAllWindows()