from tensorflow import keras
import cv2
import numpy as np
from os import listdir
import sys, time
from keras.layers import Dense, Conv2D, Input, MaxPooling2D, Flatten, Dropout
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

def get_trainimages(path, size):

    sub= 0
    train_images,train_labels= [], []
    

    for subdir in listdir(path):
        for imag in listdir(path+ "/"+ subdir):

            img= cv2.imread(path+"/"+subdir+"/"+imag,cv2.cv2.IMREAD_COLOR)
            img= cv2.resize(img, size)

            train_images.append(np.asarray(img, dtype= np.uint8))
            train_labels.append(sub)
            
       
        sub+= 1

    return [train_images,train_labels]

def get_testimages(path, size):

    sub= 0
    test_images,test_labels= [], []
   

    for subdir in listdir(path):
        for imag in listdir(path+ "/"+ subdir):

            img= cv2.imread(path+"/"+subdir+"/"+imag,cv2.IMREAD_COLOR)
            img= cv2.resize(img, size)

            test_images.append(np.asarray(img, dtype= np.uint8))
            test_labels.append(sub)
            
            
        
        sub+= 1

    return [test_images,test_labels]

[train_images,train_labels]= get_trainimages('./sort_output/train',(64,64))
[test_images,test_labels]= get_trainimages('./sort_output/test',(64,64))


train_labels= np.asarray(train_labels, dtype= np.int32)
train_images = np.asarray(train_images, dtype= np.int32)

test_labels= np.asarray(test_labels, dtype= np.int32)
test_images = np.asarray(test_images, dtype= np.int32)


train_images = train_images / 255.0
test_images = train_images / 255.0


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

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    )

datagen.fit(train_images)

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


callback = ModelCheckpoint('faces_saved_best.h5')

model.fit_generator(datagen.flow(train_images,train_labels,batch_size=1),steps_per_epoch=len(train_images)/1,epochs=200, verbose=1,callbacks=[callback])

test_loss, test_acc = model.evaluate(test_images,test_labels, verbose=0)

print('Test accuracy:', test_acc)
print('Test loss:', test_loss)
