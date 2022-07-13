import numpy as np

from builtins import range, len, int
import os
from subprocess import call
import time
import math
import config as cfg


from motor import RobotDirection

go = RobotDirection()
import cv2

from servo import Servo

servo = Servo()

from pid import PID


COLOR_LOWER = np.array([0, 43, 46])
	

COLOR_UPPER = np.array([10, 255, 255])

class Camera(object):
    def __init__(self):
        self.onoff = 0
        self.fre_count = 1
        self.px_sum = 0
        self.cap_open = 0
        self.cap = None

        self.servo_X = 7
        self.servo_Y = 8

        self.angle_X = 80
        self.angle_Y = 20


        self.X_pid = PID(0.03, 0.09, 0.0005)
        self.X_pid.setSampleTime(0.005)
        self.X_pid.setPoint(160)

        self.Y_pid = PID(0.035, 0.08, 0.002)
        self.Y_pid.setSampleTime(0.005)
        self.Y_pid.setPoint(160)


    def colorfollow(self):

        while True:
            if self.cap_open == 0:
                self.cap = cv2.VideoCapture('http://127.0.0.1:8080/?action=stream')
                self.cap_open = 1
                self.cap.set(3, 320)
                self.cap.set(4, 320)
            else:
                try:
                    ret, frame = self.cap.read()
                    if ret == 1:
                        frame = cv2.GaussianBlur(frame, (5, 5), 0)
                        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        mask = cv2.inRange(hsv, COLOR_LOWER,COLOR_UPPER)

                        mask = cv2.erode(mask, None, iterations=2)
                        mask = cv2.GaussianBlur(mask, (3, 3), 0)
                        res = cv2.bitwise_and(frame, frame, mask=mask)

                        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

                        if len(cnts) > 0:
                            cnt = max(cnts, key=cv2.contourArea)
                            (x, y), radius = cv2.minEnclosingCircle(cnt)
                            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 0, 255), 2)

                            self.X_pid.update(x)
                            self.Y_pid.update(y)
                            self.angle_X = math.ceil(
                                self.angle_X + 1 * self.X_pid.output)
                            self.angle_Y = math.ceil(
                                self.angle_Y + 0.8 * self.Y_pid.output)
                            if self.angle_X > 180:
                                self.angle_X = 180
                            if self.angle_X < 0:
                                self.angle_X = 0
                            if self.angle_Y > 180:
                                self.angle_Y = 180
                            if self.angle_Y < 0:
                                self.angle_Y = 0
                            servo.set(self.servo_X, self.angle_X)
                            servo.set(self.servo_Y, self.angle_Y)
                            self.onoff = 1
                        else:
                            pass
                except Exception as e:
                    go.stop()
                    self.cap_open = 0
                    self.cap.release()
                    print('colorfollow error:', e)

            if self.cap_open == 1 and self.onoff == 1:
                go.stop()
                self.cap_open = 0
                cfg.GRIP = 1
                self.cap.release()
                break


