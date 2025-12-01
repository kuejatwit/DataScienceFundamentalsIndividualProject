import pandas as pd
import numpy as np

# Load data from CSV file
# combine data from multiple CSV files into a single DataFrame
# saved as combined_data.csv
# convert all data types to int for consistency
# remove NA or inf values
def load_and_combine_data(file_list):
    combined_df = pd.DataFrame()
    
    for file in file_list:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    # Remove NA or inf values
    combined_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    combined_df.dropna(inplace=True)
    combined_df.reset_index(drop=True, inplace=True)
    # Ensure that the columns are named correctly and in the expected order
    expected_columns = ['analog_reading', 'muscle_state']
    if not all(col in combined_df.columns for col in expected_columns):
        raise ValueError(f"One or more expected columns are missing in the combined data. Expected columns: {expected_columns}")

    # Convert all data types to int
    combined_df = combined_df.astype(int)
    
    return combined_df

# Usage
if __name__ == "__main__":
    file_list = ['jared.csv', 'summer.csv', 'tobi.csv', 'busang.csv']  # Add more files as needed
    combined_df = load_and_combine_data(file_list)
    combined_df.to_csv('data/combined_data.csv', index=False)
    print("Combined data saved to combined_data.csv")