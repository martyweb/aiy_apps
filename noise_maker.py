#!/usr/bin/env python3

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import time
import os

button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()
#aiy.audio.get_recorder().start()

path = '/home/pi/Desktop/aiy_apps/'

os.chdir(path)

def main():
    while True:
            print('Press the button to PARTY!')
            led.set_state(aiy.voicehat.LED.ON)
            button.wait_for_press()
            print('Boom')
            led.set_state(aiy.voicehat.LED.BLINK)
            os.system("aplay DJ\ Airhorn\ Sound\ Effect.wav")
            time.sleep(1)
            
            
if __name__ == '__main__':
    main()
