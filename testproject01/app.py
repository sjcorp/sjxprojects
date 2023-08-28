# Stock Price Prediction Using LSTM
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st

import yfinance as yf
# import pandas_datareader as data
yf.pdr_override() # <== that's all it takes :-)
from pandas_datareader import data as pdr

st.title('Stock Trend Prediction')
user_input = st.text_input('Enter Stock Ticker','ICICIBANK.NS')

df = pdr.get_data_yahoo(user_input, start='2010-1-1')
df.head()

#Describing Data
st.subheader('Data from 2010-2023)')
st.write(df.describe())

#visualizations
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100,'r')
plt.plot(ma200,'b')
plt.plot(df.Close,'y')
st.pyplot(fig)

