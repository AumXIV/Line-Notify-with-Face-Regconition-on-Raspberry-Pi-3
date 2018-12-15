
from tensorflow import keras
import paho.mqtt.client as mqtt
from PIL import Image
import io
import cv2
import numpy as np
from os import listdir
import sys, time
from keras.layers import Dense, Conv2D, Input, MaxPooling2D, Flatten, Dropout
from keras.models import Model
import tensorflow as tf
from line_notify import LineNotify


ACCESS_TOKEN = "6U9HLCv5cO1z8RDS9fatkg0jVL8AUjRkpIlxJxkeALO"
notify = LineNotify(ACCESS_TOKEN)

mqttBroker = "iot.eclipse.org"   
port = 1883
keepAlive = 60

people = ['JEAN','JEK','PING','THANK']

def conv3x3(input_x,nb_filters):
    return Conv2D(nb_filters, kernel_size=(3,3), use_bias=False,
               activation='relu', padding="same")(input_x)
    
inputs = Input(shape=(64,64,3))
x = conv3x3(inputs, 32)
x = conv3x3(x, 32)
x = MaxPooling2D(pool_size=(2,2))(x) 
x = conv3x3(x, 64)
x = conv3x3(x, 64)
x = MaxPooling2D(pool_size=(2,2))(x) 
x = conv3x3(x, 128)
x = MaxPooling2D(pool_size=(2,2))(x) 
x = Flatten()(x)
x = Dense(128, activation="relu")(x)
preds = Dense(4, activation='softmax')(x)
model = Model(inputs=inputs, outputs=preds)

model.load_weights("faces_saved_best.h5")


model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


def get_predicts(path, size):

    predicts_images = []
    
    img= cv2.imread(path,cv2.IMREAD_COLOR)
    img= cv2.resize(img, size)

    predicts_images.append(np.asarray(img, dtype= np.uint8))
    predicts_images = np.asarray(predicts_images, dtype= np.int32)        
            
    predicts_images = predicts_images / 255.0   
       
    predicts = model.predict(predicts_images)
    
    classification = np.argmax(predicts[0])
    
    return classification



def Notify(classification):
    
    if classification == 0 :
        notify.send("JEAN is Coming", image_path='Send.jpg')
    elif classification == 1:
        notify.send("JEK is Coming", image_path='Send.jpg')
    elif classification == 2:
        notify.send("PI์์์NG is Coming", image_path='Send.jpg')
    elif classification == 3:
        notify.send("THANK is Coming", image_path='Send.jpg')
    else :
        notify.send("HAVE an INTRUDER", image_path='Send.jpg')



def on_message(client, userdata, msg):
    print ("Topic : ", msg.topic)
    
    
    image = Image.open(io.BytesIO(msg.payload))
    image.save("./input.jpg")
     
    color_image= cv2.imread('./input.jpg')
    [x, y]= color_image.shape[:2]
    x_factor= (float(y)/x)
    resize_y= 480

    color_image= cv2.resize(color_image, (int(resize_y* x_factor), resize_y))

    pre_image= cv2.imread('./input.jpg',cv2.IMREAD_COLOR)
    pre_image= cv2.resize(pre_image, (int(resize_y* x_factor), resize_y))
     


    frontal_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    bBoxes= frontal_face.detectMultiScale(pre_image, 
            scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), 
			flags=cv2.CASCADE_SCALE_IMAGE)

    for bBox in bBoxes:
        (p,q,r,s)= bBox

        cv2.rectangle(color_image, (p,q), (p+r,q+s), (2,255,25), 2)

        pre_crop_image= pre_image[q:q+s, p:p+r]
        pre_crop_image= cv2.resize(pre_crop_image,(256,256))
    
    cv2.imwrite('./precrop.jpg',pre_crop_image)
        
    classification = classification = get_predicts('./precrop.jpg',(64,64))

    box_text= format("Subject: "+ people[classification])

    color_image =cv2.putText(color_image, box_text, (p-20, q-5), cv2.FONT_HERSHEY_PLAIN, 1.5, (5,205,2), 2)
        
    cv2.imwrite('Send.jpg',color_image)
    
    Notify(classification)
    
    


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ping")


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed with QoS: " + str(granted_qos))   


client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(mqttBroker, port, keepAlive)

classification = classification = get_predicts('./precrop.jpg',(64,64))
client.loop_start()














