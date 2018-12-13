import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from urllib.parse import urlparse
import sys
import time
import json

def setUp(args):
    # parse mqtt url for connection details
    global url
    global auth
    url_str = args
    print(url_str)
    url = urlparse(url_str)
    base_topic = url.path[1:]
    auth=None
    # Connect
    if (url.username):
        auth = {'username':url.username, 'password':url.password}

def publishStates(green,yellow,red):
    # Publish a message
    #Create JSON strings
    greenState_json=json.dumps({"Green State = ":green, "TimeStamp = ":time.time()})
    yellowState_json=json.dumps({"Yellow State = ":yellow, "TimeStamp = ":time.time()})
    redState_json=json.dumps({"Red State = ":red, "TimeStamp = ":time.time()})

    #Create array of MQTT messages
    green_msg={"/Green State", "payload" + greenState_json}
    yellow_msg={"/Yellow State", "payload" + yellowState_json}
    red_msg={"/Red State", "payload" + redState_json}

    msgs=[green_msg,yellow_msg,red_msg]

    #Publish array of messages
    print("About to publish")
    publish.multiple(msgs, hostname=url.hostname, port=url.port, auth=auth)
    print("published")
