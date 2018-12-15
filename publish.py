#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: kobsb
"""
from subprocess import call 
from time import sleep
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
from PIL import Image


swPin = 17


delay = 10  # delay

GPIO.setmode(GPIO.BCM)     
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   


mqttBroker = "iot.eclipse.org"   
port = 1883
keepAlive = 60


def takePhoto():
    for i in range(1):
        sleep(1)    
        call(["fswebcam", "-r", "640x480", "--no-banner", "./piccam.jpg"]) 
    
def publish():
    f=open("pic1.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client.publish("ping",byteArr,0)
    

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
    

def on_publish(client, userdata, mid):
    print("published... "+str(mid))
    client.loop_stop()
   

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish


client.connect(mqttBroker, port, keepAlive)
client.loop_start()


print('running')
try:  
    while True:       
        if GPIO.input(swPin): # if port == 1  
            print("PIR is 1/HIGH/True - Take Photo") 
            takePhoto()
            publish()
            sleep(delay)            
        else:  
            print("PIR is 0/LOW/False - do nothing")  
           

        sleep(1)         
 
finally:                 
    GPIO.cleanup()       
    print("cleanup")



