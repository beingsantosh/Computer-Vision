import cv2
import time

cap = cv2.VideoCapture('myvideo.mp4')

if cap.isOpened() == False:
    print('File not found or it has codec error while capturing it')


while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:

        # it was saved with 20 per second
        time.sleep(1/20)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()