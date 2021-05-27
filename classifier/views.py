from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import csv
from tensorflow import Graph
import pandas as pd

img_height, img_width=224,224
with open('./models/labels.csv','r') as f:
    labelInfo=pd.read_csv(f)


label = labelInfo['breed'].to_numpy()
unique_breeds=np.unique(label)


model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=tf.keras.models.load_model('./models/05112021-133246-images-Adam.h5',custom_objects={'KerasLayer':hub.KerasLayer})
BATCH_SIZE=32

def process_image(file_path):
    img=tf.keras.preprocessing.image.load_img(file_path, target_size=(img_height, img_width) )
    x = image.img_to_array(img)
    x = x/255
    x=x.reshape(1,img_height, img_width,3)

    return x

def get_pred_label(prediction_probabilities):
  return unique_breeds[np.argmax(prediction_probabilities)]



def scanner(request):
    print('this view called')

    if request.method == 'POST':
        print("please")
        print(request.FILES)
        fileObj = request.FILES.get('dog')
        print("please" +fileObj.name)
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name, fileObj)
        filePathName = fs.url(filePathName)
        testimage = '.'+filePathName
        print(filePathName)

        img = process_image(testimage)
        
        
        with model_graph.as_default():
            with tf_session.as_default():
                predi=model.predict(img)

        predictedLabel = get_pred_label(predi[0])
        print(np.argmax(predi[0]))
        print('pugyo eta')
        print(predictedLabel)
        context = {'filePathName': filePathName, 'predictedLabel':predictedLabel}
        return render(request, 'classifier/scanner.html', context)
    else:
        return render(request, 'classifier/scanner.html')


  
    
    
  
