import serial
import threading

def receive_data(ser):
    while True:
        data = ser.readline()
        if data:
            print(data.decode().strip())

def send_commands(ser):
    while True:
        command = input("コマンドを入力してください（1: 開始, 0: 停止）: ")
        ser.write(command.encode('utf-8'))

ser = serial.Serial('/dev/ttyUSB0', 115200)

thread_recv = threading.Thread(target=receive_data, args=(ser,))
thread_send = threading.Thread(target=send_commands, args=(ser,))
thread_recv.start()
thread_send.start()

thread_recv.join()
thread_send.join()
