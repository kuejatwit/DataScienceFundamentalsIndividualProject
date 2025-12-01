import serial
import time

serial_port = '/dev/ttyUSB0'  # Update this to your serial port
baudrate = 115200
timeout = 1
ser = serial.Serial(serial_port, baudrate, timeout=timeout)

while True:
    data = ser.readline().decode('utf-8').rstrip()
    print(data)