import time
import paho.mqtt.client as mqtt

class SmartLightBulb:
    def __init__(self):
        self.state = False
        self.brightness_level = 100 # initially set the brightness to 100%
        
    def turn_on(self):
        self.state = True
        print("Bulb turned on.")
        
    def turn_off(self):
        self.state = False
        print("Bulb turned off.")
        
    def set_brightness(self, brightness_level):
        self.brightness_level = brightness_level
        print(f"Brightness level set to {self.brightness_level}.")
        
    def simulate_turn_on_off(self):
        print(self.state)
        if self.state:
            print("Simulating turning off the bulb...")
            time.sleep(2) # simulate turning off the bulb
            self.turn_off()
        else:
            print("Simulating turning on the bulb...")
            time.sleep(2) # simulate turning on the bulb
            self.turn_on()

# create a SmartLightBulb instance
bulb = SmartLightBulb()

# define the MQTT broker and topic names
broker_address = "localhost"
topic_receive = "smart_light_bulb/control"
topic_send = "smart_light_bulb/state"

# define callback functions for MQTT events
def on_connect(client, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(topic_receive)

# Whenever we have a message
def on_message(client, msg):
    message = msg.payload.decode()
    if message == "on":
        bulb.simulate_turn_on_off()
    elif message == "off":
        bulb.simulate_turn_on_off()
    else:
        brightness_level = int(message)
        bulb.set_brightness(brightness_level)
    client.publish(topic_send, f"{bulb.state},{bulb.brightness_level}")
    
# create an MQTT client and connect to the broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)

# start the MQTT client loop to listen for incoming messages
client.loop_forever()
