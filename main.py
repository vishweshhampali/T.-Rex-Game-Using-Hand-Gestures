from cv2 import cv2
import numpy as np 
import pyautogui


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    image = frame[0:240, 350:640]
    blur = cv2.GaussianBlur(image, (3,3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV) 

    l_b = np.array([3,29,60])
    u_b = np.array([255,255,255])
    mask = cv2.inRange(hsv,l_b,u_b)
    _, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    kernel = np.array((5,5))
    dilated = cv2.dilate(thresh, kernel, iterations=10)
    median = cv2.medianBlur(dilated, 3)
    
    largest_area = 0
    count = -1
    contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours : 
        area = cv2.contourArea(i)
        if (area>largest_area) :
            largest_area=area
            count = count + 1

    drawing = np.zeros(image.shape ,np.uint8)
    cv2.drawContours(drawing,contours, count, (0,255,0), 0)
    (x, y, w, h) = cv2.boundingRect(contours[count])
    cv2.rectangle(drawing, (x,y), (x+w,y+h), (0,0,255), 2)
    
    hull = cv2.convexHull(contours[count])
    cv2.drawContours(drawing, [hull], -1, (255,0,0), 2)

    hull = cv2.convexHull(contours[count],returnPoints=False)
    defects = cv2.convexityDefects(contours[count],hull)

    #print(cv2.contourArea(contours[count]))
    if cv2.contourArea(contours[count])>9000:
        print('JUMP')
        pyautogui.press('space')
        cv2.putText(frame,"JUMP", (115,80), cv2.FONT_HERSHEY_SIMPLEX, 2, 2, 2)
    else:
        print('NOT JUMPING')

    cv2.rectangle(frame, (350,0), (640,240), (0,255,0), 3)
    cv2.imshow('Video', frame)
    cv2.imshow('Dilated',dilated)
    cv2.imshow('Drawing',drawing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
