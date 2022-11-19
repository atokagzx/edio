#! /usr/bin/python3

import mraa
from time import sleep, time

class Motor:
    def __init__(self, pin_1, pin_2):
        self.pin_1 = mraa.Pwm(pin_1)
        self.pin_2 = mraa.Pwm(pin_2)
        self.stop()
    
    def stop(self):
        self.pin_1.enable(True)
        self.pin_2.enable(True)
        self.pin_1.write(1)
        self.pin_2.write(1)

    def disarm(self):
        self.pin_1.enable(False)
        self.pin_2.enable(False)
        self.pin_1.write(0)
        self.pin_2.write(0)

    def go(self, speed):
        '''
        apply speed to motor:
        speed = 0 -> disarm motor
        speed > 0 -> forward
        speed < 0 -> backward
        '''
        if speed == 0:
            self.disarm()
        elif speed > 0:
            self.pin_1.enable(True)
            self.pin_2.enable(False)
            self.pin_1.write(speed)
        elif speed < 0:
            self.pin_1.enable(False)
            self.pin_2.enable(True)
            self.pin_2.write(-speed)

    def __del__(self):
        self.stop()

class Servo:
    def __init__(self, pin):
        self._pin = mraa.Pwm(pin)
        self._pin.period_us(20000000)
        self._pin.enable(True)
    
    def _map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def _constraint(self, x, min, max):
        return min if x < min else max if x > max else x

    def write(self, angle: int):
        angle = self._constraint(angle, 0, 180)
        pw = self._map(angle, 0, 180, 700, 2300)
        self._pin.pulsewidth_us(pw)

    def writeMicroseconds(self, pw: int):
        self._pin.pulsewidth_us(pw)

    def detach(self):
        self._pin.enable(False)

    def __del__(self):
        self.detach()

class Robot:
    INPUTS = [31, 45, 32, 46, 33, 47]
    OUTPUTS = []
    def __init__(self):
        self._motor_a = Motor(0, 21)
        self._motor_b = Motor(20, 14)
        self._inputs = [mraa.Gpio(i) for i in self.INPUTS]
        self._outputs = [mraa.Gpio(i) for i in self.OUTPUTS]
        for i in self._inputs:
            i.dir(mraa.DIR_IN)
        for i in self._outputs:
            i.dir(mraa.DIR_OUT)
            i.write(0)
        self._motor_a.go(0)
        self._motor_b.go(0)
    
    def input(self):
        return [i.read() for i in self._inputs]
    
    def output(self, index, value):
        self._outputs[index].write(value)

    def stop(self):
        self._motor_a.stop()
        self._motor_b.stop()
    
    def go(self, y_speed, angular_speed):
        self._motor_a.go(y_speed + angular_speed)
        self._motor_b.go(y_speed - angular_speed)

    def __del__(self):
        for i in self._outputs:
            i.write(0)

if __name__ == "__main__":
    from mpu6050 import mpu6050 as MPU6050
    # mpu6050 = MPU6050(0x68, bus=1)
    # print(mpu6050.get_temp())
    robot = Robot()
    while True:
        robot.go(-0.2, 0)
        sleep(1)
        robot.go(0, 0)
        sleep(1)