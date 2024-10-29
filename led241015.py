from time import sleep
from gpiozero import LED

led = LED(17)
led.on()

while True:
    led.on()
    sleep(.2)
    led.off()
    sleep(.2)