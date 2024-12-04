# Preprocessing

- [formatat.py](./formatat.py) is used to resolve complex form of amplitude and phase (amplitude +i phase) to different column. And add label at the end of dataframe for specific activity.

- [final.py](./final.py) combines different files of same activity data into a single csv file.

- [removesubcarrier.ipynb](./removesubcarrier.ipynb) drops the amplitude and phase column of null, pilot and guard subcarriers to result in only columns of data subcarriers.

- [Preprocess.ipynb](./Preprocess.ipynb) performs preprocessing like Outlier removal, Denoising and Phase sanitization on the data subcarriers.

## Requirements
The requirements to run this code are:
- Altair
- Matplotlib
- Numpy
- Pandas
- Pywavelets