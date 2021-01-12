import cv2

## callback funtion


def draw_circle(event, x,y,flags, param):
    global pt1
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)

    pass

pt1 = (0,0)



cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

cv2.setMouseCallback('frame',draw_circle)

while True:

    ret, frame = cap.read()


    cv2.circle(frame, center=pt1, radius=70, color=(255, 0, 0), thickness=7)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()