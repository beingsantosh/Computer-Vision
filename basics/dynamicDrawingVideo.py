import cv2

## callback funtion


def draw_rectangle(event, x,y,flags, param):
    global pt2,pt1, topleft_clicked, bottomright_clicked

    # reset the rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        if topleft_clicked and bottomright_clicked:
            pt1 = (0,0)
            pt2 = (0,0)
            topleft_clicked =False
            bottomright_clicked = False

        # clicking first time
        if topleft_clicked == False:
            pt1 = (x,y)
            topleft_clicked = True

        # clicking  second time
        elif bottomright_clicked==False:
            pt2 = (x,y)
            bottomright_clicked = True
    pass


pt1 = (0,0)
pt2 = (0,0)
topleft_clicked =False
bottomright_clicked = False


cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

cv2.setMouseCallback('frame',draw_rectangle)

while True:

    ret, frame = cap.read()

    if topleft_clicked==True:
        cv2.circle(frame,center=pt1,radius=5,color=(255,0,0), thickness=-1)

    if topleft_clicked and bottomright_clicked:
        cv2.rectangle(frame, pt1,pt2, (0,255,0),3)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()