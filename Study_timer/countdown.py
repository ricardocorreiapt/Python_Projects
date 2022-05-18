#Time for the countdown
import time
#Using the Pillow Module to open image file.
from PIL import Image
from tkinter import *
def countdown(t):
    while t:
        #change this to your directory where you put the countdown
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time´s uppppp!')
    img = Image.open('stop.png')
    img.show()

t =  input('Enter the time in seconds: ')

countdown(int(t))


