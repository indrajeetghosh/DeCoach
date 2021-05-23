from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
import tensorflow.math 
from tensorflow.keras.layers import Dense , Conv1D, LSTM, MaxPooling1D, Flatten, Dropout, BatchNormalization,AveragePooling1D

#Please change the input_size dimension as per your input data and also no. of neurons in last FC layer  

def model():
    model = Sequential()
    model.add(Conv1D(32, 2, activation="relu", input_shape=(128,12)))
    model.add(MaxPooling1D(pool_size=2, strides=None, padding="valid")
    model.add(Conv1D(64, 3, activation="relu", input_shape=(128,12)))
    model.add(Flatten())
    model.add(Dense(64, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")
    return model
