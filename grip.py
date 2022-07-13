#encoding:utf-8
import smbus
import time
import os
import config as cfg



address = 0x18
bus = smbus.SMBus(1)

values1 = [0xff,1,6,0,0xff]
values2 = [0xff,1,7,0,0xff]
values3 = [0xff,1,8,0,0xff]
length1 = len(values1)
length2 = len(values2)
length3 = len(values3)
try:
    if cfg.GRIP == 1:
        for k in range(0,30):
            values3[3] = i
            bus.write_i2c_block_data(address,values3[0],values2[1:length3])
            time.sleep(0.05)
        for i in range(0,44):
            values1[3] = i
            bus.write_i2c_block_data(address,values1[0],values1[1:length1])
            time.sleep(0.05)
        for t in range(0,20):
            values2[3] = i
            bus.write_i2c_block_data(address,values2[0],values2[1:length2])
            time.sleep(0.05)
        for x in range (0,2):
            time.sleep(1.01)        #保护用，别动，已经烧了一个了
        for k in range(0,30):
            values3[3] = (60 - k)
            bus.write_i2c_block_data(address,values3[0],values2[1:length3])
            time.sleep(0.05)
        for q in range(0,2):
            time.sleep(1.01)
        for t in range(0,20):
            values2[3] = (20 - t)
            bus.write_i2c_block_data(address,values2[0],values2[1:length2])
            time.sleep(0.05)
        for i in range(0,44):
            values1[3] = (44 - i)
            bus.write_i2c_block_data(address,values1[0],values1[1:length1])
            time.sleep(0.05)
except IOError:
    print('WriteError')
    os.system('sudo i2cdetect -y 1')
