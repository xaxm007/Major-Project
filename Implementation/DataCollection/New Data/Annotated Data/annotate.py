import pandas as pd
import os
from datetime import datetime

file1 = '/Users/psubedi/Downloads/Major/preprocessing/Processed Data/saksham3_processed.csv'
# replace with your file2 path
file2 = '/Users/psubedi/Downloads/Major/preprocessing/Modified Data/saksham3_modified.csv'

# Load the input files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Initialize a new DataFrame for the output
output_df = pd.DataFrame(index=df1.index)
output_df.index.name = 'Index'

# Define the activities including 'No activity'
activities = ['Walking', 'Standing', 'Running',
              'Sitting', 'Jump', 'No activity']

# Custom function to parse timestamp


def parse_timestamp(ts):
    return datetime.strptime(ts, '%H:%M:%S:%f')


# Process the second file to detect minute changes
timestamps = df2.iloc[:, 0].apply(parse_timestamp)
previous_minute = None
activity_index = 0

activity_list = []

for timestamp in timestamps:
    current_minute = timestamp.minute

    if previous_minute is None:
        previous_minute = current_minute
        activity = activities[activity_index]
    else:
        if current_minute != previous_minute:
            activity_index = (activity_index + 1) % len(activities)
            activity = activities[activity_index]
            previous_minute = current_minute
        else:
            activity = activities[activity_index]

    activity_list.append(activity)

# Ensure the activity list is as long as df1's rows
while len(activity_list) < len(df1):
    activity_list.append(activities[activity_index])

# Trim the activity list if it's longer than df1's rows
activity_list = activity_list[:len(df1)]

# Add the activity list to the new DataFrame
output_df['Activity'] = activity_list

# Save the new DataFrame to a CSV file in the same directory as input file1
output_dir = os.path.dirname(file1)
output_file = os.path.join(output_dir, 'annotate_saksham3_processed.csv')
output_df.to_csv(output_file)

print(f"The output CSV file has been generated at {output_file}.")
