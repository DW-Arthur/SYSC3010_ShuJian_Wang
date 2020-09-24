#Sensehat emulator, where number of squares change from blue to red from -30 C to 105 C from temperature
from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)

while True:
    temperature = sense.temperature
    temperature_value = 64 * (temperature + 30)/ 135
    pixels = [red if i < temperature_value
				else blue for i in range(64)]
    sense.set_pixels(pixels)