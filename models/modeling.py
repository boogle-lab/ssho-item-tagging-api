import numpy as np
import pandas as pd
import tensorflow as tf
from models.prep import dataset
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Dropout, Conv2D, Input
from tensorflow.keras.layers import MaxPool2D, AveragePooling2D, Flatten
from tensorflow.keras.models import Model, Sequential
IMG_SIZE = 64
N_CHANNELS = 3

def run_model(data_dir, init_model = None):
    """
    :param data_dir: label별 데이터 폴더를 포함하고 있는 폴더의 경
    :return: Training History
    """
    train, label = dataset(base_dir=data_dir).get_data()
    label = tf.keras.utils.to_categorical(label, 5)
    print(len(train))
    if init_model:
        model = tf.keras.models.load_model(init_model)
        hist = model.fit(train, label,
                         validation_split=0.1,
                         verbose=1,
                         epochs=10,
                         batch_size=32)
    else:
        model = Modeling()
        hist = model.fit(train, label,
                         validation_split=0.1,
                         verbose=1,
                         epochs=10,
                         batch_size=32)
    # model.summary()
    model.save('model.h5')
    return hist

def Modeling():
    model = Sequential()
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(5, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    # model.summary()
    return model