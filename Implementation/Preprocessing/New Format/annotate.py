import pandas as pd
from datetime import datetime, timedelta

# Paths to the files
name = 'saksham'
session = '3'
type = 'nLoS'
input_file = '../Data/Wireless Eye Data/Raw Data/'+f'{type}/'+f'{name}'+f'{session}'+'.csv'  # Path to the original file
output_file = '../Data/Wireless Eye Data/Annotated Data/'+f'{type}/'+f'{name}'+f'{session}'+'_annotated.csv'  # Path for the annotated output

# Load and split the original file
original_df = pd.read_csv(input_file)
original_split_df = original_df.iloc[:, 0].str.split(';', expand=True)
original_split_df.columns = ['timestamp', 'MAC', 'subcarrier', 'amplitude', 'phase', 'RSSI', 'frame_control']

# Convert timestamp column to datetime
original_split_df['timestamp'] = original_split_df['timestamp'].apply(
    lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S:%f')
)

# Define activity list
# activities = ['Walking', 'Standing', 'Running', 'Sitting', 'Jump'] # session 1
# activities = ['Running', 'Jump', 'Sitting', 'Standing', 'Walking'] # session 2
# activities = ['Sitting', 'Jump', 'Standing', 'Walking', 'Running'] # session 3
# activities = ['Walking', 'Standing', 'Running']
# activities = ['Standing', 'Walking', 'Running']
activities = ['Running', 'Standing', 'Walking']

# Get the starting timestamp
start_time = original_split_df['timestamp'].iloc[0]

# Annotate activities
activity_labels = []
for _, row in original_split_df.iterrows():
    elapsed_time = row['timestamp'] - start_time
    if elapsed_time < timedelta(minutes=3):
        # Cycle through the activities based on elapsed minutes
        activity_index = (elapsed_time.seconds // 60) % len(activities)
        activity_labels.append(activities[activity_index])
    else:
        # Label as 'No activity' after 5 minutes
        activity_labels.append('No activity')



# Add the activity labels to the DataFrame
original_split_df['Activity'] = activity_labels

# Remove rows where activity is 'No activity'
filtered_df = original_split_df[original_split_df['Activity'] != 'No activity']

# Save the filtered DataFrame to a CSV file
filtered_df.to_csv(output_file, index=False)

print(f"The annotated file has been saved to {output_file}.")
