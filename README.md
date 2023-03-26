# IoT-Smart-Bulb
This code repo for the smart bulb simulation using MQTT and MQTT localhost broker.

These are the instructions to run the project:
1. Install Mosquitto on your local machine:

#brew install mosquitto

2. Start the mosquitto service using the bellow cmd

#brew services start mosquitto

3. Run the above python file to recieve the instructions for the operations

 #python SmartLightBulb.py

4. Run the Broker messages to operate the bulb:
"on"-> to ON the Bulb
"off"-> to OFF the bulb
"int"-> Any number to set the brightness of the bulb.

These are some sample controls:

#mosquitto_pub -h localhost -t smart_light_bulb/control -m "on"

#mosquitto_pub -h localhost -t smart_light_bulb/control -m "50"

#mosquitto_pub -h localhost -t smart_light_bulb/control -m "off"


We can aslo use the cloud brokers (like HIVEMQ) for but this project I have used a localhost instead.

