import pandas as pd
import numpy as np

# Load the uploaded CSV file
file_path = './csi_data/saksham/walk.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Create separate DataFrames for amplitude and phase
amplitudes = pd.DataFrame()
phases = pd.DataFrame()

# Process each subcarrier column
for col in data.columns[2:]:  # Starting from the third column (subcarrier data)
    # Convert complex string to Python complex number
    complex_numbers = data[col].apply(lambda x: complex(x.strip("()")))
    
    # Calculate amplitude and phase
    amplitudes[col] = np.abs(complex_numbers)
    phases[col] = np.angle(complex_numbers)

# Combine amplitudes and phases in the required order
final_data = pd.concat([amplitudes, phases], axis=1)
final_data['activity'] = 'walk'


output_data = final_data.iloc[:,:-1]
output_label = final_data.iloc[:,-1]
# Save the processed data to a new CSV file
output_data_path = './saksham/walk_data.csv'  # Replace with your desired output path
output_data.to_csv(output_data_path, index=False, header=False)

output_label_path = './saksham/walk_label.csv'  # Replace with your desired output path
output_label.to_csv(output_label_path, index=False, header=False)
print(f"Processed file saved to {output_data_path} and {output_label_path}")

