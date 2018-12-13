import paho.mqtt.client as mqtt
import urlparse
import sys
import time
#from front_wheels import Front_Wheels
from back_wheels import Back_Wheels
#front_wheels = Front_Wheels(channel=0)
print ""
print "Velocity needs to be an integer 0-100"
speed=input("Enter velocity=")
print "Duration is the amount of seconds to drive vehicle"
duration=input("Enter duration=")
back_wheels = Back_Wheels()
back_wheels.speed = speed                
back_wheels.forward(speed, duration)  #drive wheels forward
back_wheels.stop()                      #drive wheels stop
time.sleep(3)                           #for 1 second
                
back_wheels.backward(speed, duration) #drive wheels backward
back_wheels.stop()                      #drive wheels stop
time.sleep(3)  

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_message(client, obj, msg):
    print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed,  QOS granted: "+ str(granted_qos))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# parse mqtt url for connection details
url_str = sys.argv[1]
url = urlparse.urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe(base_topic+"/#", 0)
mqttc.loop_forever()

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
    try:
        if rc == green: 
                back_wheels.forward(speed, duration)  #drive wheels forward
        elif rc == yellow:
                #back_wheels.speed = speed/2
                back_wheels.forward(speed/2, duration)  #drive wheels forward
	elif rc == red:
                back_wheels.stop() 
                
    except KeyboardInterrupt:
    	back_wheels.stop()
       	#front_wheels.turn_straight()
        
print("rc: " + str(rc))