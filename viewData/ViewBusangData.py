import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from rms.rms import calculate_rms

def main():
    # Load data from CSV file
    df = pd.read_csv('busang_cleaned.csv')
    print("Data loaded from busang_cleaned.csv")
    print(df.head())
    rms_relaxed, rms_clenched = calculate_rms('busang_cleaned.csv')
    # Separate the data into two groups based on muscle_state
    relaxed_hand = df[df['muscle_state'] == 0]['analog_reading']
    clenched_hand = df[df['muscle_state'] == 1]['analog_reading']
    # Plot points on the same graph
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(relaxed_hand)), relaxed_hand, color='blue', label='Relaxed Hand', alpha=0.5)
    plt.scatter(range(len(clenched_hand)), clenched_hand, color='red', label='Clenched Hand', alpha=0.5)
    plt.title('Analog Readings for Relaxed and Clenched Hand')
    plt.xlabel('Sample Number')
    plt.ylabel('Analog Reading')
    plt.grid(True)
    plt.plot([0, len(df)], [rms_relaxed, rms_relaxed], color='blue', linestyle='--', label='RMS Relaxed Hand')
    plt.plot([0, len(df)], [rms_clenched, rms_clenched], color='red', linestyle='--', label='RMS Clenched Hand')
    plt.legend()
    # Calculate and print the mean values
    mean_relaxed = np.mean(relaxed_hand)
    mean_clenched = np.mean(clenched_hand)
    print(f"Mean Analog Reading for Relaxed Hand: {mean_relaxed}")
    print(f"Mean Analog Reading for Clenched Hand: {mean_clenched}")
    # Show the plot
    plt.show()
    return

if __name__ == "__main__":
    main()