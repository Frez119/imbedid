from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# GPIO 핀 팩토리 설정
factory = PiGPIOFactory()

# 센서 설정 (GPIO 23은 트리거, GPIO 24는 에코)
sensor = DistanceSensor(echo=24, trigger=23, pin_factory=factory)

while True:
    try:
        distance = round(sensor.distance * 100, 2)
        print(f'Distance to nearest object is {distance} cm')
        sleep(1)
    except Exception as e:
        print(f'Error: {e}')
        sleep(1)


        