import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
time.sleep(3)

while True:
    data = ser.readline()
    if data:
        acc_data = data.decode().strip().split(',')
        acc_data = [float(x) for x in acc_data if x.strip()]
        print("加速度データ: X={0:.2f}, Y={1:.2f}, Z={2:.2f}".format(*acc_data))
