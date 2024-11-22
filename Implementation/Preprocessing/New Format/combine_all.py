import os
import pandas as pd

# Directory containing the CSV files
directory = '../Data/Wireless Eye Data/Annotated Data/nLoS/'

# Output file path
output_file = 'combined2_annotated.csv'

# List to store dataframes
df_list = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('_annotated.csv'):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file without the header (column names)
        df = pd.read_csv(file_path, header=0)
        
        # Append the dataframe to the list
        df_list.append(df)
        print(filename)

# Concatenate all dataframes into one
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new CSV file without the header
combined_df.to_csv(output_file, index=False)

print(f"Combined CSV file has been saved to {output_file}.")
