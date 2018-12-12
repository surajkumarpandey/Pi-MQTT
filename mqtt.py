#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("lock")

def on_message(client, userdata, msg):
  if(msg.payload.decode()=='1'):  
    p.ChangeDutyCycle(12.5)  # turn towards 180 degree
    print(msg.payload.decode())
      #time.sleep(1) # sleep 1 second
  elif(msg.payload.decode()=='0'):
    print(msg.payload.decode())
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    #client.disconnect()
  else:  
    print(msg.payload.decode())
  
client = mqtt.Client()
client.connect("172.16.117.138",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
