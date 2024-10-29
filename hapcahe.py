from gpiozero import Robot, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# GPIO 핀 팩토리 설정
factory = PiGPIOFactory()

# 거리 센서 설정 (GPIO 23은 트리거, GPIO 24는 에코)
sensor = DistanceSensor(echo=24, trigger=23, pin_factory=factory)

# DC 모터 설정
dc_motor = Robot(left=(6, 12), right=(11, 9))

# 거리 임계값 설정 (센티미터)
THRESHOLD_DISTANCE = 20

while True:
    # 거리 측정 (센티미터 단위)
    distance = round(sensor.distance * 100, 2)
    print(f'Distance to object: {distance} cm')
        
        # 물체가 가까이 있을 때 (임계값보다 가까울 때)
    if distance < THRESHOLD_DISTANCE:
        print("Object detected! Starting motor")
        dc_motor.forward(speed=1)
    else:
        print("Object is far away. Stopping motor")
        dc_motor.stop()
            
    time.sleep(0.5)
        