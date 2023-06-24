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

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class SearchImage(APIView):
    def post(self, request: Request):
        # img = Image.open('/content/drive/MyDrive/data project/final images/10/10.jpg')
        # if 'image' not in request.files:
        #     return 'please try again'

        image = request.FILES.get('image', None)
        if image is None:
            return Response({'details': 'image not exist in the request'})
        img = Image.open(image)
        # print(img)

        # display(img.resize((100,100)))
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = img_array[np.newaxis, :]

        # print(img_array)
        from keras.models import load_model

        saved_model = load_model("./imageSearch/model33.h5") 
        prob = saved_model(img_array)
       

        pred = np.argmax(prob)

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

        return Response({'category': dic[pred]})
        # return jsonify({'hi': 'there'})