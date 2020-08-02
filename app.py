# -- coding: utf-8 --

# $ docker build -t flask-application:latest .
# $ docker run -d -p 5000:5000 flask-application

from flask import Flask, request, jsonify
from predict import pretrained, resize

# Flask Server Endpoint 설정
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

flask_host = "0.0.0.0"
flask_port = "5000"

@app.route("/tagging", methods=['POST'])
def item_tagging():

    data = request.get_json()

    #현재 test data
    classes = {0 : 'casual', 1 : 'cute', 2 : 'genderless', 3:'hip', 4:'modern',
               5:'monotone', 6:'street', 7:'vintage'}

    #image 경로에서 이미지를 불러와 resize된 이미지 array return
    image = resize('./data/validation_pic/carhartt overall.jpg')

    #weight : model.h5 / image : esized image
    predicted = pretrained("model.h5", image)

    print(predicted, classes[predicted[0]])

    tag = classes[predicted[0]];

    return tag

if __name__ == "__main__":

    # Run Flask Server
    app.run(host=flask_host, port=flask_port, debug=True)
