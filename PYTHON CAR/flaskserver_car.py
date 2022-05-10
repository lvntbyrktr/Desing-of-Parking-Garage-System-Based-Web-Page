import RPi.GPIO as GPIO
import time
from flask import Flask, request
from flask_cors import CORS,cross_origin
from multiprocessing import Process, Value
import requests

GPIO.setmode(GPIO.BCM)

motor1 = 24
motor2 = 25
enable1 = 23

motor3 = 8
motor4 = 7
enable2 = 12


GPIO.setwarnings(False)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(enable1,GPIO.OUT)
GPIO.setup(motor3, GPIO.OUT)
GPIO.setup(motor4, GPIO.OUT)
GPIO.setup(enable2,GPIO.OUT)

app = Flask(__name__)
#cors is used to allow http request between different servers.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#main page path
#for testing
@app.route('/')
def hello():
    return 'Welcome to Smart Garage System!'


@app.route('/api/button')
def butFunc():
    direction= request.args.get('val')
    if(direction=="go"):
        print("go")
        GPIO.output(enable1,GPIO.HIGH)
        GPIO.output(motor1,GPIO.HIGH)
        GPIO.output(motor2,GPIO.LOW)
        
        GPIO.output(enable2,GPIO.HIGH)
        GPIO.output(motor3,GPIO.LOW)
        GPIO.output(motor4,GPIO.HIGH)
        return "OK"
    elif(direction=="stop"):
        GPIO.output(enable1,GPIO.LOW)

        GPIO.output(enable2,GPIO.LOW)
       
        return "OK"
    elif(direction=="right"):
        GPIO.output(enable1,GPIO.HIGH)
        GPIO.output(motor1,GPIO.HIGH)
        GPIO.output(motor2,GPIO.LOW)
        
        
        GPIO.output(enable2,GPIO.HIGH)
        GPIO.output(motor3,GPIO.HIGH)
        GPIO.output(motor4,GPIO.LOW)
        print("right")
        return "OK"
    elif(direction=="left"):
        print("left")
        GPIO.output(enable1,GPIO.HIGH)
        GPIO.output(motor1,GPIO.LOW)
        GPIO.output(motor2,GPIO.HIGH)
        
        GPIO.output(enable2,GPIO.HIGH)
        GPIO.output(motor3,GPIO.LOW)
        GPIO.output(motor4,GPIO.HIGH)
        return "OK"
    else:
        print("back")
        GPIO.output(enable1,GPIO.HIGH)
        GPIO.output(motor1,GPIO.LOW)
        GPIO.output(motor2,GPIO.HIGH)
        
        GPIO.output(enable2,GPIO.HIGH)
        GPIO.output(motor3,GPIO.HIGH)
        GPIO.output(motor4,GPIO.LOW)
        return "OK"

if __name__=='__main__':
    app.run(host='0.0.0.0', port= 6060)


