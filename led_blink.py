from re import M, T
import mraa
from time import sleep, time
### Motor ###
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

# motor_a = Motor(0, 21)
# motor_b = Motor(20, 14)
# motor_a.go(-0.1)
# motor_b.go(-0.1)
# sleep(5)

# EN_PIN = mraa.Pwm(9)
# IN1_PIN = mraa.Gpio(8)
# IN2_PIN = mraa.Gpio(7)
# print(dir(EN_PIN))
# EN_PIN.period(10000) 
# IN1_PIN.dir(mraa.DIR_OUT)
# IN2_PIN.dir(mraa.DIR_OUT)
# def backward(speed):
#     EN_PIN.write(speed)
#     IN1_PIN.write(False)
#     IN2_PIN.write(True)
# def forward(speed):
#     EN_PIN.write(speed)
#     IN1_PIN.write(True)
#     IN2_PIN.write(False)



# IN1_PIN.write(1)
# IN2_PIN.write(0)
# for i in range(50):
#     try:
#         x = mraa.Pwm(i)
#         # x.dir(mraa.DIR_OUT)
#         # x.write(0)
#     except:
#         print("Error: GPIO " + str(i) + " not found")
#     else:
#         print("GPIO " + str(i) + " found")
# servo_pin = mraa.Pwm(3)
# servo_pin.period_us(20000000) 
# servo_pin.enable(True)
# while True:
#     for i in range(700, 2000, 1):
#         servo_pin.pulsewidth_us(i)
#         time.sleep(0.001)
# gpio_1 = mraa.Gpio(32)
# gpio_1.dir(mraa.DIR_IN)
# while True:
#     print(gpio_1.read())


### Serial port example  ###
# port = "/dev/ttyMFD1"

# data = 'Hello Mraa!'

# uart = mraa.Uart(port)
# uart.setBaudRate(115200)
# uart.write(bytearray(data, 'utf-8'))
# uart.setMode(8, mraa.UART_PARITY_NONE, 1)
# uart.setFlowcontrol(False, False)

# while True:
#     if uart.dataAvailable():
#         data_byte = uart.readStr(1)
#         print(data_byte)
#         if data_byte == "X":    
#             uart.writeStr("Yes, master!")
# from smbus2 import SMBus
# wire = SMBus(1)
# h = wire.read_byte_data(0x68, 0x41)
# l = wire.read_byte_data(0x68, 0x42)
# value = (h << 8) + l
# if (value >= 0x8000):
#     value = -((65535 - value) + 1)
# print(value)
# actual_temp = (value / 340.0) + 36.53
# print(actual_temp)
# b = bus.read_byte_data(80, 0)
# wire = mraa.I2c(1, raw=True)
# wire.address(0x68)
# # wire.write(0x6B)
# # wire.write(0x00)
# sleep(0.1)
# print(wire.read(1))

### MPU6050 ###
# from mpu6050 import mpu6050 as MPU6050
# mpu6050 = MPU6050(0x68, bus=1)
# print(mpu6050.get_temp())

PIN1 = 31
PIN2 = 45
PIN3 = 32
PIN4 = 46
PIN5 = 33
PIN6 = 47
gpio_1 = mraa.Gpio(PIN5)
gpio_1.dir(mraa.DIR_IN)
while True:
    print(gpio_1.read())