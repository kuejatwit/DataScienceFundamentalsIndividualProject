import serial 
import time
import pandas as pd

port = '/dev/ttyUSB0'  # Update this to your serial port
baudrate = 115200 # Set baudrate for serial communication
timeout = 1 # Set timeout for serial communication

# Initialize serial connection
ser = serial.Serial(port, baudrate, timeout=timeout)
# Initialize dataset dictionary
dataset = {"analog_reading": [], "muscle_state": []} 
# Collect data for relaxed and clenched hand
print("Relaxed Hand") 
# Wait before starting data collection
for i in range(0,5):
    print("Starting in", 5 - i)
    time.sleep(1)
# Flush input buffer
ser.flushInput()
for i in range(0,10000):
    try: #try to avoid decode errors if non-UTF-8 characters are received
        data = ser.readline().decode('utf-8').rstrip()
        print(i ,data)
        dataset["analog_reading"].append(data)
        dataset["muscle_state"].append(0)
    except UnicodeDecodeError: # if decode error occurs, skip that line
        print("Decoding error, skipping this line.")
        continue
ser.flushInput()
# Collect data for clenched hand
print("Clench Hand")
# Wait before starting data collection
for i in range(0,5):
    print("Starting in", 5 - i)
    time.sleep(1)
    ser.flushInput()
# Collect data for clenched hand
for i in range(0,10000):
    # Read and decode data from serial port
    try: #try to avoid decode errors if non-UTF-8 characters are received
        data = ser.readline().decode('utf-8').rstrip()
        print(i ,data)
        dataset["analog_reading"].append(data)
        dataset["muscle_state"].append(1)
    except UnicodeDecodeError: # if decode error occurs, skip that line
        print("Decoding error, skipping this line.")
        continue
# Save dataset to CSV
df = pd.DataFrame(dataset)
df.to_csv('data/tobi.csv', index=False)
print("Data saved to tobi.csv")
print(df.head())