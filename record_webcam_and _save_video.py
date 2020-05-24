import base64

import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while True:
    retval, image = cap.read()
    ret, jpeg_image = cv2.imencode('.jpg',image)
    jpg_as_text = base64.b64encode(jpeg_image)
    nparr = np.frombuffer(base64.b64decode(jpg_as_text), np.uint8)
    image5 = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
    cv2.imshow('frame',image5)
    cv2.imshow('frame1', image)
    out.write(image)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        out.release()
        break
cap.release()
cv2.destroyAllWindows()