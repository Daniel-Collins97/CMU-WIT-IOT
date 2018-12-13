from time import sleep
from gpiozero import LED
import client_pub_mult as push
import sys

redLED = LED(18)
yellowLED = LED(19)
greenLED = LED(20)

greenState=None
redState=None
yellowState=None

push.setUp(sys.argv[1])

while True:
    #Green light off, yellow light on for 10 seconds
    print("Green off, Yellow on, 10 sec")
    print("-----------------------------")
    greenLED.off()
    yellowLED.on()
    greenState=greenLED.is_lit
    yellowState=yellowLED.is_lit
    redState=redLED.is_lit
    push.publishStates(greenState,yellowState,redState)
    sleep(10)


    #Yellow light off, red light on for 30 seconds
    print("Yellow off, Red on, 30 sec")
    print("-----------------------------")
    yellowLED.off()
    redLED.on()
    greenState=greenLED.is_lit
    yellowState=yellowLED.is_lit
    redState=redLED.is_lit
    push.publishStates(greenState,yellowState,redState)
    sleep(30)

    #Red light off, green light on for 40 seconds
    print("Red off, Green on, 40 sec")
    print("-----------------------------")
    redLED.off()
    greenLED.on()
    greenState=greenLED.is_lit
    yellowState=yellowLED.is_lit
    redState=redLED.is_lit
    push.publishStates(greenState,yellowState,redState)
    sleep(40)

