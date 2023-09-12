from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Hardware LEDs
led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

# GUI Definitions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Event Functions
def toggle_led(led1, led1_button):
    if led1.is_lit:
        led1.off()
        led1_button["text"] = "Red On"
    else:
        led1.on()
        led1_button["text"] = "Red Off"

def toggle_led(led2, led2_button):
    if led2.is_lit:
        led2.off()
        led2_button["text"] = "Green On"
    else:
        led2.on()
        led2_button["text"] = "Green Off"

def toggle_led(led3, led3_button):
    if led3.is_lit:
        led3.off()
        led3_button["text"] = "Blue On"
    else:
        led3.on()
        led3_button["text"] = "Blue Off"

def close():
    GPIO.cleanup()
    win.destroy()

# Widgets for LED 1
led1_button = Button(win, text='Turn LED 1 On', font=myFont, command=lambda: toggle_led(led1, led1_button),
bg='red', height=1, width=24)
led1_button.grid(row=0, column=0)

# Widgets for LED 2
led2_button = Button(win, text='Turn LED 2 On', font=myFont, command=lambda: toggle_led(led2, led2_button),
bg='green', height=1, width=24)
led2_button.grid(row=1, column=0)

# Widgets for LED 3
led3_button = Button(win, text='Turn LED 3 On', font=myFont, command=lambda: toggle_led(led3, led3_button),
bg='blue', height=1, width=24)
led3_button.grid(row=2, column=0)

# Exit Button
exit_button = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exit_button.grid(row=3, column=0)

win.protocol("WM_DELETE_WINDOW", close)  # Exit cleanup
win.mainloop()  # Main loop
