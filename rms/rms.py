import pandas as pd
import numpy as np

def calculate_rms(file_path):
    # Load data from CSV file
    df = pd.read_csv(file_path)
    
    # Separate the data into two groups based on muscle_state
    relaxed_hand = df[df['muscle_state'] == 0]['analog_reading']
    clenched_hand = df[df['muscle_state'] == 1]['analog_reading']
    
    # Calculate RMS values
    rms_relaxed = np.sqrt(np.mean(relaxed_hand**2))
    rms_clenched = np.sqrt(np.mean(clenched_hand**2))
    
    return rms_relaxed, rms_clenched
if __name__ == "__main__":
    file_path = 'jared.csv'  # Update with your actual file path
    rms_relaxed, rms_clenched = calculate_rms(file_path)
    print(f"RMS Analog Reading for Relaxed Hand: {rms_relaxed}")
    print(f"RMS Analog Reading for Clenched Hand: {rms_clenched}")

def compare_rms(data, clenched_rms, relaxed_rms):
    if abs(data - clenched_rms) < abs(data - relaxed_rms):
        return 0
    elif abs(data - clenched_rms) > abs(data - relaxed_rms):
        return 1
    else:
        return -1