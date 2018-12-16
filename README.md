# Line Notify with Face Regconition on Raspberry Pi 3

About Project 
------------------------------------

- This project is about an online intruder alert system with facial recognition (Face Recognition) on raspberry pi 3

- Inside the system, there is a motion sensor detecting heat from humans or animals. When the sensor detects a human or animal within a range of 1-5 meters (set up), the system automatically records incoming faces.

- system will submission system image with The MQTT protocol,image will processed by the Computer Server to determine who is coming in the room.

- When the process is complete, the person who comes to be identified. The system will send a notification message and the processed image to the user's line.

Overview
-------------------
![](https://www.picz.in.th/image/overview.9Byq6z)



Implementation
--------------------------------------
1. Run file **publish.py** in raspberry pi

2. When the program is running and connect with **Mqtt Broker** it will print **"CONNACK received with code 0"** , leave the program open

3. Train the datasets in the **Train.py** file prepared on the server.

4. Run the **Subscribe.py** file on your server

5. When the program is connected to MQTT Broker and the Subscribe topic will print**"Connected with result code 0"**and**''Subscribe with QOS (0,)"**. leave the program open.

6. When Motion Sensor captures the movement that people have come to. The camera will work. And send image to MQTT Broker

7. When the server receives an image from Rasp Pi, the program will display the topic of the received information.

8. The program will take the image from the rasp pi to process it to detect the person's page and identify it as the data we have trained. 

9. When the process is finished,program with create image file is Processed,detected and identified.And send those alerts and pictures to the User via the line.
