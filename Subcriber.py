#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:05:38 2020

@author: saviraagustin
"""

import paho.mqtt.client as mqtt
import time

broker="192.168.43.252"
port= 1975

def onconnect(client,userdata,flags,rc):
    print("connected OK")


def ondisconnect(client,userdata,flags,rc=0):
    print("disconnected ")

def onsubscribe(client,userdata,mid,granted_qos):
    print("Subscribed")
    
def onmessage(client, userdata, msg):
    print("message received : "+str(msg.payload.decode()))
    print("message topic :"+str(msg.topic))

client = mqtt.Client()

client.on_connect = onconnect
client.on_disconnect = ondisconnect
client.on_subscribe = onsubscribe
client.on_message = onmessage

print("connecting to broker "+str(broker))

client.connect(broker, port)

client.loop_start()

client.subscribe("Test/test",0)

time.sleep(5)
client.loop_stop()
client.disconnect()