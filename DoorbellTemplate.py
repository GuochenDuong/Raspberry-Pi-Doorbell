from slacker import Slacker #pip install slacker (in cmd)
from dot3k import joystick
from dot3k import lcd
from dot3k import backlight
from time import sleep
from picamera import PiCamera
import warnings
import json
import requests
camera = PiCamera()

warnings.filterwarnings('ignore', category=DeprecationWarning)


slack = Slacker('')#Your Bot's AUTH TOKEN GOES HERE

#"""Pings a message and photo to slack and sends a welcome message to the person waiting at the door"""

@joystick.on(joystick.BUTTON)
def door(pin):
    payload ={"text": "Ding Dong!\nThere's someone at the door!"}# the first announcement
    backlight.rgb(155,155,155)
    lcd.write("Welcome!")#message for display 'o tron 3000 white spacing to account for screen
    sleep(3)
    lcd.clear()
    sleep(1)
    lcd.write("Please wait...  We shall be     right with you.")
    sleep(1)
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/image.jpg')#takes and saves picture to this directory ON THE PI
    camera.stop_preview()
    ping = requests.post('X',data=json.dumps(payload))#where X is your web hook integration, then pings message
    slack.files.upload('/home/pi/image.jpg', channels = '#doorbell')#uploads photo
    sleep(10)
    payload={"text": "C'mon they're waiting...:hourglass:"}#reminder 1
    ping = requests.post('X',data=json.dumps(payload))
    sleep(10)
    payload={"text": "Time's a tickin'! Answer the door already!!!:rage::anger:"}#reminder 2
    ping = requests.post('X',data=json.dumps(payload))
    sleep(10)
    payload={"text": "Well if they're gone it's all of your fault, good job guys.:unamused:"}#final reminder
    ping = requests.post('https://hooks.slack.com/services/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',data=json.dumps(payload))
    lcd.clear()
    backlight.off()

@joystick.on(joystick.DOWN)#flashy colours test delete at your whim
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
        
