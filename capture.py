import os
import datetime
import sys
import time
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(5,GPIO.OUT)
# read the absolute path
script_dir = os.path.dirname('/home/pi/Desktop/db/')

        
while True:
        time.sleep(1)
        if(GPIO.input(11)==1):
                time.sleep(1)
                print ('smile!!')
                # call the .sh to capturthe image
                os.system('./webcam.sh')#get the date and time, set the date and time as a filename.
                currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
                # create the real path
                rel_path = currentdate +".jpg"
                #  join the absolute path and created file name
                abs_file_path = os.path.join(script_dir, rel_path)
                print (abs_file_path)
                
        else:
                print("Noone")        
