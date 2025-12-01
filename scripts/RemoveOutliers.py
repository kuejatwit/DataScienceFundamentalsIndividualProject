import pandas as pd
import numpy as np

def removeOutliers(input_file, output_file):
    try:
        # Load data
        df = pd.read_csv(input_file)

        Q1 = df['analog_reading'].quantile(0.25)
        Q3 = df['analog_reading'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df['analog_reading'] >= lower_bound) & (df['analog_reading'] <= upper_bound)]

        # Filter outliers
        df_clean = df[(df['analog_reading'] >= lower_bound) & (df['analog_reading'] <= upper_bound)]

        # Save cleaned data
        df.to_csv(output_file, index=False)
        print(f"Data cleaned and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage
removeOutliers('busang_cleaned.csv', 'busang_outliersRemoved.csv')