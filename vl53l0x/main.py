import time
import board
import busio
import adafruit_vl53l0x
import asyncio
from easysense import Easysense


class Vl53l0x(Easysense):

    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(i2c)
        self.vl53.start_continuous()

    def give_data(self):
        distance = self.vl53.range
        return {"Distance": distance}
