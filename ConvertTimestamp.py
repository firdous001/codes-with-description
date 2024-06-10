import pandas as pd
import os
from datetime import datetime

# Define the folder containing the CSV files
folder_path = 'C:/Users/Firdos/Downloads/drive-download-20240609T182838Z-001/extractedAI'


# Define the function to convert timestamp format
def convert_timestamp_format(timestamp):
    # Parse the original timestamp
    original_format = datetime.strptime(timestamp, "%Y-%m-%d_%H-%M-%S")

    # Extract components and format manually
    month = original_format.month
    day = original_format.day
    year = original_format.year
    hour = original_format.hour
    minute = original_format.minute

    # Convert 24-hour format to 12-hour format and determine AM/PM
    am_pm = 'AM'
    if hour >= 12:
        am_pm = 'PM'
    if hour > 12:
        hour -= 12
    if hour == 0:
        hour = 12

    # Construct the new timestamp format
    new_format = f"{month}/{day}/{year} {hour}:{minute:02d} {am_pm}"
    return new_format


# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Convert the Timestamp column
        df['Timestamp'] = df['Timestamp'].apply(convert_timestamp_format)

        # Save the updated DataFrame back to CSV
        df.to_csv(file_path, index=False)

print("Timestamp format conversion completed for all CSV files.")
