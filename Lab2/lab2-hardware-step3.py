#Sensehat emulator, where number of squares change from blue to red from -30 C to 105 C from temperature
from sense_emu import sense_emu

sense = SenseHat()

red = (0, 255, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)

while True:
    temperature = sense.temperature
    temperature_value = 64 * (temperature + 135)/ 30
    pixels = [blue if i < temperature_value
				else red for i in range(64)]
    sense.set_pixels(pixels)