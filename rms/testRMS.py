import serial 
import time
import pandas as pd
from rms import calculate_rms, compare_rms

port = '/dev/ttyUSB0'  # Update this to your serial port
baudrate = 115200 # Set baudrate for serial communication
timeout = 1 # Set timeout for serial communication
user = input("Enter your name: ").lower()
clenched_rms, relaxed_rms = calculate_rms(f'{user}.csv')

# Initialize serial connection
ser = serial.Serial(port, baudrate, timeout=timeout)
# Initialize dataset dictionary
dataset = {"analog_reading": [], "muscle_state": [], "predicted_state": []} 
# Collect data for relaxed and clenched hand
print("Relaxe Hand") 
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
        dataset["predicted_state"].append(compare_rms(int(data), clenched_rms, relaxed_rms))
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
        dataset["predicted_state"].append(compare_rms(int(data), clenched_rms, relaxed_rms))
    except UnicodeDecodeError: # if decode error occurs, skip that line
        print("Decoding error, skipping this line.")
        continue
# Save dataset to CSV
df = pd.DataFrame(dataset)
df.to_csv(f'{user}.csv', index=False)
print(f"Data saved to {user}.csv")
print(df.head())