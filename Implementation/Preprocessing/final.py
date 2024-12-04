import pandas as pd
import os

# Define the base directory and folder names
base_path = './format/'
folders = ['aavash', 'abashesh', 'ashish', 'prashant', 'saksham']

# Define the output file path
output_file = './final/walk_data.csv'

# Initialize an empty list to store the DataFrames
data_frames = []

# Iterate through each folder and read the 'run.csv' file
for folder in folders:
    file_path = os.path.join(base_path, folder, 'walk_data.csv')  # Construct the path to run.csv
    try:
        # Read the CSV file and add it to the list
        df = pd.read_csv(file_path, header=None)  # Adjust header if needed
        data_frames.append(df)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Concatenate all the DataFrames
if data_frames:
    concatenated_df = pd.concat(data_frames, ignore_index=True)
    # Save the concatenated DataFrame to a CSV file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure the output directory exists
    concatenated_df.to_csv(output_file, index=False, header=False)
    print(f"Concatenated file saved to {output_file}")
else:
    print("No files were found or concatenated.")
