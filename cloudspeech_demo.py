#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import time
import mysql.connector
import mysql


def main():

    

    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize().strip()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            #aiy.audio.say(text)
            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'blink' in text:
                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'who is the best boss' in text:
                aiy.audio.say('searching')
                time.sleep(2)
                aiy.audio.say('Kevin is')
            
            elif 'how many completed stories do I have' in text:
                
                
                aiy.audio.say('Searching')
                print('Searching')
                
                status = 'Completed'
                rows = getcounts(status)
                
                if len(rows) == 0:
                    message = "Sorry, you have nothing " + status
                    aiy.audio.say(message)
                    print(message)
                else:
                    
                    for x in rows:
                        message = "You have " + str(x[0]) + " stories " + status
                        aiy.audio.say(message)
                        print(message)
            
            elif 'get story status' in text:
                print('Please say story number...')
                aiy.audio.say('Say the story number')
                text2 = recognizer.recognize().replace(' ','')
                aiy.audio.say('Searching for U S ' + text2)
                print('Searching for U S ' + text2)
                
                rows = getdata('US', text2)
                
                if len(rows) == 0:
                    message = "Sorry, the search did not find anything"
                    aiy.audio.say(message)
                    print(message)
                else:
                    message = "The search found " + str(len(rows)) + " rows"
                    aiy.audio.say(message)
                    print(message)
                    for x in rows:
                        message = "The status of " + x[0]+ " is " + x[1]
                        aiy.audio.say(message)
                        print(message)
                    
                
            elif 'goodbye' in text:
                break


def getdata(type, id):
    cnx = mysql.connector.connect(host='localhost', user='pi', passwd='martyweb', db='tu')
    cursor = cnx.cursor()

    query = ("SELECT *  FROM tu.agile_central "
                 "WHERE id='%s%s'") % (type, id)

    #hire_start = datetime.date(1999, 1, 1)
    #hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query)
    rows = cursor.fetchall()      

    cursor.close()
    cnx.close()
    return rows

def getcounts(status):
    cnx = mysql.connector.connect(host='localhost', user='pi', passwd='martyweb', db='tu')
    cursor = cnx.cursor()

    query = ("SELECT count(*)  FROM tu.agile_central "
                 "WHERE status='%s'") % (status)
    
    cursor.execute(query)
    rows = cursor.fetchall()      


    cursor.close()
    cnx.close()
    return rows


if __name__ == '__main__':
    main()
