from engi1020.arduino.api import *
m = 255/800
y = 0
x = analog_read(6)
l = int(m * (x-y) + 0)
pin = 3

print(l)
oled_print(f'Light: {l}')
analog_write(pin, int(127))