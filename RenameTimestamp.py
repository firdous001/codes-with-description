
import pandas as pd
import os

# Path to the folder containing the CSV files
folder_path = "C:/Users/Firdos/Downloads/drive-download-20240609T182838Z-001/extractedAI"

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a CSV
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Rename the column if it exists
        if 'timestamp' in df.columns:
            df.rename(columns={'timestamp': 'Timestamp'}, inplace=True)

            # Save the modified DataFrame back to CSV
            df.to_csv(file_path, index=False)

print("Column renaming completed.")
