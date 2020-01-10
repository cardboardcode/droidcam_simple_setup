import numpy as np
import cv2

http = 'http://'
ip_address = '192.168.2.27'
url =  http + ip_address + ':4747/video'
# Opening video stream of ip camera via its url
cap = cv2.VideoCapture(url)

# Corrective actions printed in the even of failed connection.
if cap.isOpened() is not True:
    print ('Not opened.')
    print ('Please ensure the following:')
    print ('1. DroidCam is not running in your browser.')
    print ('2. The IP address given is correct.')

# Connection successful. Proceeding to display video stream.
while cap.isOpened() is True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Turning your frames into grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    # cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
