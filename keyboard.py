from djitellopy import tello
import pygame
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

axis_threshold = 0.5


def getKeyboardInput():
    pygame.event.pump()

    axis_0 = joystick.get_axis(0)  # Axis 0 (left-right)
    axis_1 = joystick.get_axis(1)  # Axis 1 (up-down)

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if axis_0 < -axis_threshold:
        lr = -speed
    elif axis_0 > axis_threshold:
        lr = speed
    if axis_1 < -axis_threshold:
        fb = speed
    elif axis_1 > axis_threshold:
        fb = -speed
    if joystick.get_button(0):
        ud = speed
    elif joystick.get_button(1):
        ud = -speed
    if joystick.get_button(4):
        yv = -speed
    elif joystick.get_button(5):
        yv = speed
    if joystick.get_button(9):
        me.land()
        sleep(3)
    if joystick.get_button(8):
        me.takeoff()
    if joystick.get_button(3):
        me.flip_left()
    return [lr, fb, ud, yv]


while True:
    pygame.event.pump()
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
