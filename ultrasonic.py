# coding:utf-8
import time
from builtins import int, chr, object

import gpio as gpio
import config as cfg

from motor import RobotDirection
go = RobotDirection()

from servo import Servo
servo = Servo()



class Ultrasonic(object):
	def __init__(self):
		self.MAZE_ABLE = 0
		self.MAZE_CNT = 0
		self.MAZE_TURN_TIME = 0
		self.dis = 0
		self.s_L = 0
		self.s_R = 0

	def get_distance(self):

		time_count = 0
		time.sleep(0.01)
		gpio.digital_write(gpio.TRIG, True)
		time.sleep(0.000015)
		gpio.digital_write(gpio.TRIG, False)
		while not gpio.digital_read(gpio.ECHO):
			pass
		t1 = time.time()
		while gpio.digital_read(gpio.ECHO):
			if time_count < 2000:
				time_count = time_count + 1
				time.sleep(0.000001)
				pass
			else:
				print("NO ECHO receive! Please check connection")
				break
		t2 = time.time()
		distance = (t2 - t1) * 340 / 2 * 100
		if distance < 500:
			cfg.DISTANCE = round(distance, 2)
			return cfg.DISTANCE
		else:
			cfg.DISTANCE = 0
			return 0

	def avoidbyragar(self):
		cfg.LEFT_SPEED = 30
		cfg.RIGHT_SPEED = 30
		dis = self.get_distance()
		if 25 < dis < 300 or dis == 0:
			cfg.AVOID_CHANGER = 1
		else:
			if cfg.AVOID_CHANGER == 1:
				go.stop()
				cfg.AVOID_CHANGER = 0

	def send_distance(self):
		dis_send = int(self.get_distance())
		print(dis_send)

	def maze(self):
		cfg.LEFT_SPEED = 35
		cfg.RIGHT_SPEED = 35
		self.dis = self.get_distance()
		if self.MAZE_ABLE == 0 and ((self.dis > 30) or self.dis == 0):
			while ((self.dis > 30) or self.dis == 0) and cfg.CRUISING_FLAG:
				self.dis = self.get_distance()
				go.forward()
			if cfg.CRUISING_FLAG:
				self.MAZE_CNT = self.MAZE_CNT+1
				print(self.MAZE_CNT)
				go.stop()
				time.sleep(0.05)
				go.back()
				time.sleep(0.15)
				go.stop()
				time.sleep(0.05)
				if self.MAZE_CNT > 3:
					self.MAZE_CNT = 0
					self.MAZE_ABLE = 1

		else:
			go.stop()
			self.s_L = 0
			self.s_R = 0
			time.sleep(0.1)
			servo.set(7, 5)
			if cfg.CRUISING_FLAG:
				time.sleep(0.25)
			self.s_R = self.get_distance()
			if cfg.CRUISING_FLAG:
				time.sleep(0.2)

			servo.set(7, 175)
			if cfg.CRUISING_FLAG:
				time.sleep(0.3)
			self.s_L = self.get_distance()
			if cfg.CRUISING_FLAG:
				time.sleep(0.2)
			servo.set(7, 80)
			time.sleep(0.1)

			if (self.s_R == 0) or (self.s_R > self.s_L and self.s_R > 20):
				self.MAZE_ABLE = 0
				cfg.LEFT_SPEED = 99
				cfg.RIGHT_SPEED = 99
				go.right()
				if cfg.CRUISING_FLAG:
					time.sleep(cfg.MAZE_TURN_TIME/1000)
				cfg.LEFT_SPEED = 45
				cfg.RIGHT_SPEED = 45

			elif (self.s_L == 0) or (self.s_R < self.s_L and self.s_L > 20):
				self.MAZE_ABLE = 0
				cfg.LEFT_SPEED = 99
				cfg.RIGHT_SPEED = 99
				go.left()
				if cfg.CRUISING_FLAG:
					time.sleep(cfg.MAZE_TURN_TIME/1000)
				cfg.LEFT_SPEED = 45
				cfg.RIGHT_SPEED = 45

			else:
				self.MAZE_ABLE = 1
				go.back()
				if cfg.CRUISING_FLAG:
					time.sleep(0.3)

			go.stop()
			time.sleep(0.1)
