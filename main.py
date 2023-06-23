from flask import Flask, request, jsonify
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
# from keras.preprocessing.image import ImageDataGenerator
# from keras.applications import VGG16
# from keras import models, layers, optimizers
# import matplotlib.image as mpimg
# import math
# import os
from PIL import Image
# import keras.utils as image
# import tensorflow as tf




app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    # img = Image.open('/content/drive/MyDrive/data project/final images/10/10.jpg')
    if 'image' not in request.files:
        return 'please try again'
    img = Image.open(request.files.get('image'))
    # print(img)

    # display(img.resize((100,100)))
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array[np.newaxis, :]

    # print(img_array)
    from keras.models import load_model
    saved_model = load_model("./model33.h5") 
    try:
        prob = saved_model(img_array)
    except Exception as e:
        print(f'------{e}')

    pred = np.argmax(prob)
    print(pred)
    dic = { 0: 'AMULET',
            1: 'HUMAN MUMMY',
            2: 'JAR',
            3: 'JEWELLERY',
            4: 'MASK',
            5: 'RELIEF',
            6: 'SEAL',
            7: 'SHABTI',
            8: 'STATUE',
            9: 'STELA',
            10: 'VASE',
            11: 'WALL PAINTING'}
    print(dic[pred])
    return jsonify({'category': dic[pred]})
    # return jsonify({'hi': 'there'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)