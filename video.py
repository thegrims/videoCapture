import numpy as np
import cv2

# for i in range(3):
#     capture = cv.CaptureFromCAM(i)
#     if capture: break

cap = cv2.VideoCapture(0)
print(cap)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        print("no frame read")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()