#18	4
#23	17
import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(18, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(4, gpio.OUT)


def reverse(tf):
	
	gpio.output(17, True)
	gpio.output(23, False)

	gpio.output(18, True)
	gpio.output(4, False)
	time.sleep(tf)
	gpio.cleanup()
	

def forward(tf):
	
	gpio.output(17, False)
	gpio.output(23, True)
	gpio.output(18, False)
	gpio.output(4, True)
	time.sleep(tf)
	gpio.cleanup()
	

def turn_right(tf):
	#18	4
	#23 	17
	
	gpio.output(17, True)
        gpio.output(18, False)
        gpio.output(23, True)
        gpio.output(4, False)
        time.sleep(tf)
        gpio.cleanup()
def turn_left(tf):
	
	gpio.output(17, False)
        gpio.output(18, True)
        gpio.output(23, False)
        gpio.output(4, True)
        time.sleep(tf)
        gpio.cleanup()
def key_input(event):
	init()
	print 'Key:', event.char
	key_press = event.char
	sleep_time = 2.030
	
	if key_press.lower() == 'w':
		forward(sleep_time - 1)
	elif key_press.lower() =='s':
		reverse(sleep_time - 1)
	elif key_press.lower() == 'a':
		turn_left(sleep_time)
	elif key_press.lower() == 'd':
		turn_right(sleep_time)
	else:
		gpio.cleanup()
	
	
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()



