import pandas as pd
import numpy as np
# Load data from CSV file
# Remove NA or inf values
# remove double quotes
# try to converts all data to integers
# if an error occurs, handle it gracefully
# Save cleaned data to new CSV file
def clean_data(input_file, output_file):
    try:
        # Load data
        df = pd.read_csv(input_file)

        # Remove NA or inf values
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)

        # Remove double quotes from string columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.replace('"', '')

        # Convert all data to integers where possible
        for col in df.columns:
            try:
                df[col] = df[col].astype(int)
            except ValueError:
                # If conversion fails, delete rows with non-integer values
                df = df[pd.to_numeric(df[col], errors='coerce').notnull()]
                df[col] = df[col].astype(int)

        # Save cleaned data
        df.to_csv(output_file, index=False)
        print(f"Data cleaned and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage
clean_data('data/busang.csv', 'data/cleaned_busang.csv')