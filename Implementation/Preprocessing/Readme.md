## Visualization of Collected Data
This is the current code for data collection visualization phase.

- [Visualization](./Visualization.ipynb) 
    - This file plots ```Amplitude``` for all subcarriers, ```PCA components```, ```Spectrogram```.
- [Conversion](./Conversion.ipynb)
    - Data conversion file for [ErmonGroup](https://github.com/ermongroup/Wifi_Activity_Recognition) and [Ludlows](https://github.com/ludlows/CSI-Activity-Recognition) csv format.
- [PCANote](./PCANote.ipynb)
    - Implementation by [psubedi0424](https://github.com/psubedi0424) for `Hampel` filter and visualization of Data
## Requirements
The requirements to run this code are:
- Numpy
- Pandas
- Matplotlib
- Scikit-Learn

##
1. ```Create a conda env```
```sh
conda create -n <your_environment_name>
```

2. ```Install requirements```
```sh
pip install -r requirement.txt
```

3. ```Install Ipykernel for using JupyterNotebook```
```sh
conda install ipykernel
```

4. ```Connect new ipykernel to the conda env```
```sh
python -m ipykernel install --user --name <your_env_name> --display-name "<new_name_for_your_kernel"
```

## #Note:
```Recommended to create conda environment for this project.```