import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import json
from time import sleep
from gpiozero import LED


def setUp(args):
    # Define event callbacks
    def on_connect(client, userdata, flags, rc):
        print("Connection Result: " + str(rc))

    def on_publish(client, obj, mid):
        print("Message ID: " + str(mid))
    global mqttc
    global base_topic
    mqttc = mqtt.Client()

    # Assign event callbacks
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish

    # parse mqtt url for connection details
    url_str = sys.argv[1]
    print(url_str)
    url = urlparse(url_str)
    base_topic = url.path[1:]

    # Connect
    if (url.username):
        mqttc.username_pw_set(url.username, url.password)
    mqttc.connect(url.hostname, url.port)
    mqttc.loop_start()
    
def publishStates(state, timeLeft):
    states_json=json.dumps({"state":state, "time_entered":time.time(), "time_in_state":timeLeft})
    mqttc.publish(base_topic+"/lightStates", states_json)