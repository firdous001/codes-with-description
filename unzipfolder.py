import os
import zipfile
import shutil

def extract_csv_from_folders(zip_file_path, output_folder):
    # Temporary folder to extract the top-level zip file
    temp_folder = 'temp_extracted'

    # Create the temporary folder if it doesn't exist
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Extract the top-level zip file
    with zipfile.ZipFile(zip_file_path, 'r') as top_zip:
        top_zip.extractall(temp_folder)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each folder in the temporary extraction folder
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    for member in zip_ref.namelist():
                        if member.endswith('.csv'):
                            zip_ref.extract(member, output_folder)
                            print(f"Extracted {member} to {output_folder}")

    # Clean up the temporary folder
    shutil.rmtree(temp_folder)

# Replace 'zip_file_path' and 'output_folder' with your actual file path and output folder
zip_file_path = r'C:\Users\Firdos\Downloads\drive-download-20240609T182838Z-001.zip'
output_folder = r'C:\Users\Firdos\Downloads\drive-download-20240609T182838Z-001\extractedAI'

extract_csv_from_folders(zip_file_path, output_folder)
