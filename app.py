# -- coding: utf-8 --

# $ docker build -t flask-application:latest .
# $ docker run -d -p 5000:5000 flask-application

from flask import Flask, request, jsonify
from predict import pretrained, resize
# url to img requirements
from urllib.request import urlopen
import cv2
import numpy as np

# Flask Server Endpoint 설정
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

flask_host = "0.0.0.0"
flask_port = "5000"


# url -> img return
def url_to_img(url):
    # PIL version
    # resp = requests.get(url, stream = True)
    # resp.raw.decode_content = True
    # img = Image.open(resp.raw)

    # opencv-python version
    resp = urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # array 형태의 img를 반환합니다.
    return img

@app.route("/tagging", methods=['GET'])
def item_tagging():
    url = ""

    ## TODO: url을 읽어서 아래에 resize함수에서 처리할수 있도록 부탁드립니다.
    """
    TAGGING WITH URL VERSION
    image = resize(url_to_img(url))
    """
    # 현재 test data
    classes = {0: 'casual', 1: 'cute', 2: 'genderless', 3: 'hip', 4: 'modern',
               5: 'monotone', 6: 'street', 7: 'vintage'}

    # image 경로에서 이미지를 불러와 resize된 이미지 array return
    image = resize('./data/validation_pic/carhartt overall.jpg')

    # weight : model.h5 / image : esized image
    predicted = pretrained("model.h5", image)

    print(predicted, classes[predicted[0]])

    tag = classes[predicted[0]]

    return tag


if __name__ == "__main__":
    # Run Flask Server
    app.run(host=flask_host, port=flask_port, debug=True)
