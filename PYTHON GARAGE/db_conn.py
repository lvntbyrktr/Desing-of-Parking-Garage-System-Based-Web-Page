import time
import requests
import sys
import RPi.GPIO as GPIO
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_light_sensor_v1_2 import GroveLightSensor

gas = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(gas,GPIO.IN)
GPIO.setwarnings(False)

light = GroveLightSensor(2)

ultrasonic = GroveUltrasonicRanger(16)

#check gase sensor's value mq2
def checkGase():
    if GPIO.input(19):
        return 0
    else:
        return 1
def sendToServer(payload):
    headers = {'content-type': 'application/x-www-form-urlencoded','accept':'/','user-agent': 'my-app/0.0.1'}
    r = requests.post("http://smartgarageproject.com/rpi_post.php", data=payload, headers=headers)
    return r.status_code

while True:
    gas_veri=checkGase()
    ldr_veri=light.light
    ultrasonic_veri=ultrasonic.get_distance()
    print(gas_veri)
    print(ldr_veri)
    print(int(ultrasonic_veri))
    data = {"gas":gas_veri,"light":ldr_veri,"ult":ultrasonic_veri}
    print("  ")
    httpcode = sendToServer(data)
    print(httpcode)
    time.sleep(1)

