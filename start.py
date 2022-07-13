import config as cfg
import servo
import os
from ultrasonic import Ultrasonic
ultrasonic = Ultrasonic()
from camera import Camera
camera = Camera()
import time

if cfg.CRUISING_FLAG == 1:
    servo.set(1, 165)
    servo.set(2, 15)
    servo.set(3, 90)
    servo.set(4, 90)
    servo.set(7, 90)
    servo.set(8, 0)
    ultrasonic.avoidbyragar()
    time.sleep(0.5)
    ultrasonic.send_distance()
    time.sleep(1)
    ultrasonic.maze()
    time.sleep(0.05)
    os.system("python camera.py")
    camera.colorfollow()
    while True:
        if cfg.GRIP == 1:
            os.system("python grip.py")
            break
    time.sleep(0.05)
    ultrasonic.maze()
