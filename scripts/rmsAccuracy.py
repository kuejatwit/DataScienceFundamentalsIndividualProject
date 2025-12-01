import numpy as np
import pandas as pd

# Compute the accuracty of RMS values against known data
def rms_accuracy(file_path, rms_relaxed, rms_clenched):
    # Load data from CSV file
    df = pd.read_csv(file_path)
    # Separate the data into two groups based on muscle_state
    relaxed_hand = df[df['muscle_state'] == 0]['analog_reading']
    clenched_hand = df[df['muscle_state'] == 1]['analog_reading']
    # Calculate accuracy for relaxed hand
    correct_relaxed = np.sum(np.abs(relaxed_hand - rms_relaxed) < np.abs(relaxed_hand - rms_clenched))
    accuracy_relaxed = correct_relaxed / len(relaxed_hand) if len(relaxed_hand) > 0 else 0
    # Calculate accuracy for clenched hand
    correct_clenched = np.sum(np.abs(clenched_hand - rms_clenched) < np.abs(clenched_hand - rms_relaxed))
    accuracy_clenched = correct_clenched / len(clenched_hand) if len(clenched_hand) > 0 else 0
    return accuracy_relaxed, accuracy_clenched
if __name__ == "__main__":
    # Example usage
    file_path = 'data/busangTestRMS.csv'  # Update with your file path
    rms_relaxed = 150  # Example RMS value for relaxed hand
    rms_clenched = 300  # Example RMS value for clenched hand
    accuracy_relaxed, accuracy_clenched = rms_accuracy(file_path, rms_relaxed, rms_clenched)
    print(f"Accuracy for Relaxed Hand: {accuracy_relaxed * 100:.2f}%")
    print(f"Accuracy for Clenched Hand: {accuracy_clenched * 100:.2f}%")
