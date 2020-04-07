#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:06:31 2020

@author: saviraagustin
"""

import paho.mqtt.client as mqtt
import time

broker="192.168.43.252"
port = 1975

def onconnect(client,userdata,flags,rc):
    print("Connected OK")

def ondisconnect(client,userdata,flags,rc=0):
    print("Disconnected" )

def onpublish(client,userdata,mid):
    print("Publishing")

client = mqtt.Client()  

client.on_connect = onconnect
client.on_disconnect = ondisconnect
client.on_publish = onpublish

print("Connecting to broker "+str(broker))

client.connect(broker, port)

client.loop_start()
    
client.publish("Test/test","Bismillah",0)

time.sleep(5)
client.loop_stop()
client.disconnect()