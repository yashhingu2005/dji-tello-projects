import cv2
import numpy as np
from PIL import Image
import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit


# read webcam
frameWidth = 640
frameHeight = 480
webcam = cv2.VideoCapture(0)
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)
deadZone = 100

yellow = [0, 255, 255]
llmt, ulmt = get_limits(color=yellow)
# visualize webcam
while True:
    ret, frame = webcam.read()

    hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvimg, llmt, ulmt)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    # boundary
    cv2.circle(frame, (int(frameWidth / 2), int(frameHeight / 2)), 5, (0, 0, 255), 5)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        cx = int(x1 + (x2 / 2))
        cy = int(y1 + (y2 / 2))

        if (cx < int(frameWidth / 2) - deadZone):
            cv2.putText(frame, " GO LEFT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            write_read('r')
            cv2.rectangle(frame, (0, int(frameHeight / 2 - deadZone)),
                          (int(frameWidth / 2) - deadZone, int(frameHeight / 2) + deadZone), (0, 0, 255), cv2.FILLED)
        elif (cx > int(frameWidth / 2) + deadZone):
            cv2.putText(frame, " GO RIGHT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            write_read('l')
            cv2.rectangle(frame, (int(frameWidth / 2 + deadZone), int(frameHeight / 2 - deadZone)),
                          (frameWidth, int(frameHeight / 2) + deadZone), (0, 0, 255), cv2.FILLED)
        elif (cy < int(frameHeight / 2) - deadZone):
            cv2.putText(frame, " GO UP ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            write_read('u')
            cv2.rectangle(frame, (int(frameWidth / 2 - deadZone), 0),
                          (int(frameWidth / 2 + deadZone), int(frameHeight / 2) - deadZone), (0, 0, 255), cv2.FILLED)
        elif (cy > int(frameHeight / 2) + deadZone):
            cv2.putText(frame, " GO DOWN ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            write_read('d')
            cv2.rectangle(frame, (int(frameWidth / 2 - deadZone), int(frameHeight / 2) + deadZone),
                          (int(frameWidth / 2 + deadZone), frameHeight), (0, 0, 255), cv2.FILLED)

    cv2.imshow('frame', mask)

    # cv2.imshow('hsv', hsvimg)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
