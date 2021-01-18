#acting and Saving Video Frames using OpenCV-PythonPython
import cv2

# Opens the Video file
cap= cv2.VideoCapture('dronev6.mp4')
i=0
j=0
while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == False:
        break
    if j%200 == 0:
        cv2.imwrite('./frames/dronev6_'+str(i)+'.jpg',frame)
        i+=1
    j+=1

cap.release()
cv2.destroyAllWindows()

