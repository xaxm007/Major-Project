## Data Format
The data was collected for `walking`, `standing`, `running`, `sitting`, `jumping`. Each activity were performed for `1 minute` so, the each session consists data of `5 minutes` for `3 person`.

Following are the order of activities for each session.
- Session_1:
    - `walking`, `standing`, `running`, `sitting`, `jumping`.

- Session_2:
    - `running`, `jumping`, `sitting`, `standing`, `walking`.

- Session_3:
    - `sitting`, `jumping`, `standing`, `walking`, `running`.

## File Content
- [ModifiedData](./Modified%20Data/)
    - This folder contains dataset where csv file includes `timestamp` for labelling.
- [ProcessedData](./Processed%20Data/)
    - This folder contains dataset where csv file contains `52 Data Subcarriers (1-26, 38-63)`, removing `Pilot (27, 39, 53)`, `Guard (0, 28-37)` and `DC(32) subcarriers`.