import cv2
import base64
import time

cap = cv2.VideoCapture(0)
retval, image = cap.read()
time.sleep(3)
cap.release()

# Convert captured image to JPG
ret, buffer = cv2.imencode('.jpg', image)

# Convert to base64 encoding and show start of data
jpg_as_text = base64.b64encode(buffer)
print(jpg_as_text[:80])

# Convert back to binary
jpg_original = base64.b64decode(jpg_as_text)

# Write to a file to show conversion worked
with open('test.jpg', 'wb') as f_output:
    f_output.write(jpg_original)