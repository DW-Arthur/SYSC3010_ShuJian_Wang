from sense_hat import SenseHat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import time

s = SenseHat()
s.low_light = True


x = 0

list  = ["D", "W"]

def pushed_any(event):
  global x
  if event.action == "pressed":
    s.show_letter(str(list[x % len(list)]))
    x+=1

s.stick.direction_any = pushed_any

while True: 
    
    time.sleep(.75)
    