import zipfile
import os

# Step 1: Specify the path to your ZIP file
zip_file_path = r'C:\Users\lubab\Downloads\Archive.zip'

import os

file_contents_dict = {}

# Step 4: Open the ZIP file and read the contents
with zipfile.ZipFile(zip_file_path, 'r') as zip:
    # Iterate over each file in the ZIP archive
    for file_name in zip.namelist():
        base_name = os.path.basename(file_name)  # Get the base file name without path
        if base_name.endswith('.txt'):  # Only process .txt files
            # Open the file within the ZIP and read its content
            with zip.open(file_name) as file:
                file_contents_dict[base_name.replace('.txt', '')] =[line.strip() for line in file.read().decode('utf-8').splitlines()]