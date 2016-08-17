from slacker import Slacker #pip install slacker
from dot3k import joystick
from dot3k import lcd
from dot3k import backlight
from time import sleep
from picamera import PiCamera
import json
import requests
camera = PiCamera()


slack = Slacker('xoxp-69711970307-69760058800-69825018663-5d922b650f')

"""Pings a message and photo to slack and sends a welcome message to the person waiting at the door"""

@joystick.on(joystick.BUTTON)
def door(pin):
    payload ={"text": "Ding Dong!\nThere's someone at the door!"}
    backlight.rgb(155,155,155)
    lcd.write("Hello!          Welcome to      Deeson!")#white spacing to account for screen
    sleep(3)
    lcd.clear()
    sleep(1)
    lcd.write("Please wait...  Stand in front  of camera.")
    sleep(1)
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/image.jpg')#saves picture to this directory
    camera.stop_preview()
    ping = requests.post('https://hooks.slack.com/services/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',data=json.dumps(payload))#pings message
    slack.files.upload('/home/pi/image.jpg', channels = '#doorbell')#uploads photo
    lcd.clear()
    lcd.write("Your request is being processed ...")
    sleep(1)
    payload={"text": "C'mon they're waiting...:hourglass:"}
    ping = requests.post('https://hooks.slack.com/services/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',data=json.dumps(payload))
    sleep(1)
    payload={"text": "Time's a tickin'! Answer the door already!!!:rage::anger:"}
    ping = requests.post('https://hooks.slack.com/services/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',data=json.dumps(payload))
    sleep(1)
    payload={"text": "Well if they're gone it's all of your fault, good job guys.:unamused:"}
    ping = requests.post('https://hooks.slack.com/services/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',data=json.dumps(payload))
    lcd.clear()
    backlight.off()
@joystick.on(joystick.LEFT)#photo function test
def photo(pin):
    camera.start_preview()
    sleep(2)
    camera.stop_preview()
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    slack.files.upload('/home/pi/image.jpg', channels = '#doorbell')
    slack.chat.post_message('@chen','ping')
    
@joystick.on(joystick.UP)#video function test
def vid(pin):
    camera.start_preview()
    camera.start_recording('/home/pi/Vid.h264')
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()

"""@joystick.on(joystick.RIGHT)
def ping(pin):"""
    

@joystick.on(joystick.DOWN)#flashy colours test
def party(pin):
    r = 0
    g = 0
    b = 0
    count = 0
    partyup = True
    while partyup == True:
        count = count + 1
        r = 15* count
        g = 15* (count-8)
        b = 15* (count - 15)
        backlight.rgb(r,g,b)
        backlight.off()
        sleep(0.01)
        if count ==16:
            partyup = False
        
