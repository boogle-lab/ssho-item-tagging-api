import tensorflow as tf
import cv2
import numpy as np

IMG_SIZE = 64

def pretrained(weights, image) :

    model = tf.keras.models.load_model(weights)
    predicted_class = model.predict_classes(image)

    return predicted_class

def resize(image_path) :

    temp = cv2.imread(image_path).astype(np.float64)
    img = cv2.resize(temp, (IMG_SIZE, IMG_SIZE))
    img = np.expand_dims(img, axis=0)

    return img

if __name__ == "__main__" :

    #현재 test data
    classes = {0 : 'casual', 1 : 'cute', 2 : 'genderless', 3:'hip', 4:'modern',
               5:'monotone', 6:'street', 7:'vintage'}

    #image 경로에서 이미지를 불러와 resize된 이미지 array return
    image = resize('./data/validation_pic/carhartt overall.jpg')

    #weight : model.h5 / image : esized image
    predicted = pretrained("model.h5", image)

    print(predicted, classes[predicted[0]])