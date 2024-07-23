import streamlit as st
import joblib 
import sklearn
import pandas as pd
import numpy as np

model=joblib.load('kath_lr.pkl')
features = joblib.load('kath_lr_cols.pkl')

def pred(new_data):
    x = model.predict(new_data)
    return x
sepal_length = st.number_input("Enter sepal length")
sepal_width = st.number_input("Enter sepal width")
petal_length = st.number_input("Enter petal length")
petal_width = st.number_input("Enter petal width")

if st.button('predict'):
    new_data=pd.DataFrame(
        {
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width]   
        }
    )

    p=pred(new_data[features])

    st.write(f'the predicted value is {p[0]}')