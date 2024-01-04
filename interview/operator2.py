import math


class shape:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"length is {self.length}"


class square(shape):
    def __init__(self, length):
        super().__init__(length)

    def cal_area(self):
        area = math.pow(self.length, 2)

    def cla_crc(self):
        crc = 4 * self.length

    def __str__(self):
        return f"circumferance is {self.cla_crc()}, area is {self.cal_area()}"
