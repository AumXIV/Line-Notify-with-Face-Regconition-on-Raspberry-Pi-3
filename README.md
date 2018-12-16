# Line Notify with Face Regconition on Raspberry Pi 3


About Project 
------------------------------------

- This project is about an online intruder alert system with face recognition  on raspberry pi 3

- Inside the system, there is a motion sensor detecting heat from humans or animals. When the sensor detects a human or animal within a range of 1-5 meters (set up), the system automatically records incoming faces.

- system will submission system image with The MQTT protocol,image will processed by the Computer Server to determine who is coming in the room.

- When the process is complete, the person who comes to be identified. The system will send a notification message and the processed image to the user's line.

Overview
-------------------

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/overview.PNG)
      

Hardware List
------------------
1. Raspberry Pi 3
2. Webcam Camera 
3. Motion Sensor HC-SR501 PIR

 **How to connect PIR HC-SR501 with Raspberry Pi 3**

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/hardware.png)

Implementation
--------------------------------------
1. Run file **publish.py** in raspberry pi

2. When the program is running and connect with **MQTT Broker** it will print **"CONNACK received with code 0"** , leave the program open

3. Train the datasets in the **Train.py** file prepared on the server.

4. Run the **Subscribe.py** file on your server

5. When the program is connected to **MQTT Broker** and the Subscribe topic will print **"Connected with result code 0"** and **''Subscribe with QOS (0,)"**. leave the program open.

6. When Motion Sensor captures the movement that people have come to. The camera will work. And send image to MQTT Broker

7. When the server receives an image from Rasp Pi, the program will display the topic of the received information.

8. The program will take the image from the rasp pi to process it to detect the person's page and identify it as the data we have trained. 

9. When the process is finished,program with create image file is Processed,detected and identified.And send those alerts and pictures to the User via the line.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/Send.jpg)
![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/line.jpg)

Prepare Dataset 
--------------------------

1. Take all the image with have trainer's face. Put them in the **input** folder within the same project.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/dataset1.PNG)

2. Run the **detect_face_datasets.py** file to get only face-specific images in the **output** folder (create a prepared folder).

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/dataset2.PNG)

3. Extract all the **output** files from the **output** folder into the **sort_output folder**, divided equally for the Train and Test, and split the files into folders named without the need to rename them.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/datasets3%20.PNG)
![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/dataset4.PNG)
![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/dataset5.PNG)

Line Notify
----------------------

1. Open [https://notify-bot.line.me/en/](https://notify-bot.line.me/en/ "https://notify-bot.line.me/en/") login with our user and password line

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/line%201.PNG)

2. Get token for sending data to the Line by putting Token into the Python program we want to used for send.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/line%202.PNG)

3. Give name the sender that will show who sent the message and choose whether to send the message to anyone, only us or as a group.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/line%203.PNG)

4. Copy the token to keep.

![](https://github.com/pingnuttakrid/Line-Notify-with-Face-Regconition-on-Raspberry-Pi-3/blob/master/readme/line%204%20.PNG)

Provider
---------------

Nuttakrid Uppatumwipanon
Bachelor's degree in electronics and telecommunication engineering
king mongkut's university of technology thonburi
Student id 58070502476

project in ENE490 Machine Learning

