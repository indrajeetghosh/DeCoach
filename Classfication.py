from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
import tensorflow.math 
from tensorflow.keras.layers import Dense , Conv1D, LSTM, MaxPooling1D, Flatten, Dropout, BatchNormalization,AveragePooling1D

#Please change the input_size dimension as per your input data and also no. of neurons. 

def model():
    model = Sequential()
    model.add(Conv1D(256,35,input_shape=(numOfRows, numOfColumns),activation='relu'))
    model.add(Dropout(0.60))
    model.add(Conv1D(200,25,input_shape=(numOfRows, numOfColumns),activation='relu'))
    model.add(Dropout(0.65))
    model.add(Conv1D(200,20,input_shape=(numOfRows, numOfColumns),activation='relu'))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.65))
    learning_rate = 0.0003
    epoch= 300
    decay_rate = learning_rate / epoch
    momentum = 0.99
    sgd = optimizers.SGD(lr=learning_rate, momentum=momentum, decay=decay_rate, nesterov=False)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    return model
