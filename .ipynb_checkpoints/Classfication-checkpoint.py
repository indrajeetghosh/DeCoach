from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
import tensorflow.math 
from tensorflow.keras.layers import Dense , Conv1D, LSTM, MaxPooling1D, Flatten, Dropout, BatchNormalization,AveragePooling1D

#Please change the input_size dimension as per your input data and also no. of neurons. 

def model():
    model = Sequential()
    model.add(Conv1D(256,9,input_shape=(128,12),activation='relu'))
    model.add(MaxPooling1D(pool_size=2, strides=None, padding="valid"))
    model.add(Dropout(0.75))
    model.add(Conv1D(128,15,input_shape=(128,12),activation='relu'))
    model.add(MaxPooling1D(pool_size=2, strides=None, padding="valid"))
    model.add(Dropout(0.1))
    model.add(Conv1D(64,15,input_shape=(128,12),activation='relu'))
    model.add(Dropout(0.75))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(12, activation='softmax'))
    learning_rate = 0.0003
    decay_rate = learning_rate / 400
    momentum = 0.99
    sgd = optimizers.SGD(lr=learning_rate, momentum=momentum, decay=decay_rate, nesterov=False)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    return model
