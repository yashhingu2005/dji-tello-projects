import cv2

import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


# read webcam
frameWidth = 640
frameHeight = 480
webcam = cv2.VideoCapture(0)
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)
deadZone = 100

face_cascade = cv2.CascadeClassifier('C:/Users/Admin/PycharmProjects/tello/haarcascade_frontalface_default.xml')

yellow = [0, 255, 255]
# visualize webcam
while True:
    ret, frame = webcam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(grey, 1.3, 1)
    for (x, y, w, h) in face:
        # To draw a rectangle in a face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = grey[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

    cv2.imshow('frame', frame)

    # cv2.imshow('hsv', hsvimg)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
