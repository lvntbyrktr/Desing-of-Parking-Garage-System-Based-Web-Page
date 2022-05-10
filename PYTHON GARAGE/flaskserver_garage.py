import RPi.GPIO as GPIO
import time
from flask import Flask, request
from flask_cors import CORS,cross_origin
from multiprocessing import Process, Value
import requests

GPIO.setmode(GPIO.BCM)
motor1 = 24
motor2 = 25
enable = 23
fan = 21 #pin 40, fan
led = 14 #pin 8, led

GPIO.setup(led,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(enable,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
#pwm will be generated for the led to light at different levels.
led_pwm = GPIO.PWM(led,500)
led_pwm.start(0) # first situation is off

#its same for fan
fan_pwm = GPIO.PWM(fan,100)
fan_pwm.start(0)

app = Flask(__name__)
#cors is used to allow http request between different servers.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#main page
#for testing
@app.route('/')
def hello():
    return 'Welcome to Smart Garage System!'

@app.route('/api/fan')
def fanFunc():
    action = request.args.get('action')
    fan_speed = int(request.args.get('fan_speed'))
    fan_status = int(request.args.get('fan_status'))
    if (action == "on" and fan_status == 1):
        fan_pwm.ChangeDutyCycle(fan_speed)
        print(f"Fan on {fan_speed}")
        return "OK"
    else:
        fan_pwm.ChangeDutyCycle(0)
        print("Fan off")
        return "OK"
    return "OK"
@app.route('/api/led')
def ledFunc():
    action = request.args.get('action')
    brightness = int(request.args.get('led_brightness'))
    led_status = int(request.args.get('led_status'))
    print(led_status)
    if (action == "on" and led_status == 1):
        led_pwm.ChangeDutyCycle(brightness)
        print("LED ON")
        
        return "OK"
    elif (action == "off" and led_status == 0 ):
        led_pwm.ChangeDutyCycle(100)
        print("LED OFF")
        return "OK"
if __name__=='__main__':
    app.run(host='0.0.0.0', port= 6060)

