import cv2
import numpy as np
import serial
import time

ser=serial.Serial('COM4',9600)
time.sleep(2)

# 코 검출 데이터
nose_cascade = cv2.CascadeClassifier('./haarcascade_mcs_nose.xml')

cap = cv2.VideoCapture(1)
ds_factor = 1.0

# 프로그램 실행
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 코 검출

    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in nose_rects:
        cv2.putText(frame, "please wear your mask", (20,50), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0,0,255))
        ser.write(b'H')
        break

    ser.write(b'L')
    cv2.imshow('Nose Detector', frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        ser.write(b'L')
        print("프로그램 종료")
        break

cap.release()
cv2.destroyAllWindows()