import cv2
import numpy as np

#########################################
## drawing circle on each click #########
#########################################

def draw_circle(event,x,y, flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 50,(0,255,0),-1)


cv2.namedWindow(winname = 'my_pic')

cv2.setMouseCallback('my_pic', draw_circle)


########################################
### showing window via opencv ##########
########################################

img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_pic', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()