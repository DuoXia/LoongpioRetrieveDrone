# coding:utf-8

import numpy as np


CRUISING_FLAG = 1
PRE_CRUISING_FLAG = 0

ANGLE_MAX = 160
ANGLE_MIN = 15

LEFT_SPEED = 80
RIGHT_SPEED = 80
LASRT_LEFT_SPEED = 100
LASRT_RIGHT_SPEED = 100

SERVO_NUM = 1
SERVO_ANGLE = 90
SERVO_ANGLE_LAST = 90
ANGLE = [90, 90, 90, 90, 90, 90, 90, 0]

DISTANCE = 0
AVOID_CHANGER = 1
AVOIDDROP_CHANGER = 1

MAZE_TURN_TIME = 400

CAMERA_MOD = 0
LINE_POINT_ONE = 320
LINE_POINT_TWO = 320
GRIP = 0

VREF = 5.12
POWER = 3
LOOPS = 0
PS2_LOOPS = 0

PROGRAM_ABLE = True

COLOR_LOWER = [
	np.array([0, 43, 46]),
	np.array([35, 43, 46]),
	np.array([100, 43, 46]),
	np.array([125, 43, 46]),
	np.array([11, 43, 46])
]

COLOR_UPPER = [
	np.array([10, 255, 255]),
	np.array([77, 255, 255]),
	np.array([124, 255, 255]),
	np.array([155, 255, 255]),
	np.array([25, 255, 255])
]
COLOR_FOLLOW_SET = {'red': 0, 'green': 1, 'blue': 2, 'violet': 3, 'orange': 4}
COLOR_INDEX = 0
