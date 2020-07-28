import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from tqdm.auto import tqdm
import os

IMG_SIZE = 64
N_CHANNELS = 3

# Only train
class dataset():
    def __init__(self, base_dir = ''):
        self.base_dir = base_dir

    def resize(self, imgs, size=IMG_SIZE):
        resized = []
        for img in imgs:
            resized.append(cv2.resize(img, (size, size)))
        return resized

    def load_dataset(self):
        images = []
        labels = []
        for i in tqdm(range(5)):
            dir = os.listdir(self.base_dir)[i]
            path = os.path.join(self.base_dir, dir)
            for img in os.listdir(path):
                # print(img)
                temp = cv2.imread(os.path.join(path, img))
                images.append(temp)

                labels.append(i)
        images = self.resize(images)
        return images, labels

    def get_data(self):
        data, label = self.load_dataset()
        data = np.array(data) # Array -> Normalize, reshape
        data = data/255.0 # Normalize
        data = data.reshape(-1, IMG_SIZE, IMG_SIZE, N_CHANNELS)
        # print(data[:5])

        return data, label
