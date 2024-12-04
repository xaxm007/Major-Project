# Model Training

- Model is trained in Pytorch Framework.
- The model consists of 2 BiLSTM layers with 1 Attention Layer.
- The data is divided based on a sliding window method which selects a fixed length of rows to create training data where each window slides with a fixed length of step.