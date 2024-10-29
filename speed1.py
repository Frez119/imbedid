from gpiozero import Robot
import time

dc_motor = Robot(left=(6, 12), right=(11, 9))

for num in range(4):
    print(num, "Forward 회전")
    dc_motor.forward(speed=1)
    time.sleep(3)
    print("모터 정지")
    dc_motor.stop()
    time.sleep(0.5)
    print(num, "Backward 회전")
    dc_motor.backward(speed=0.5)
    time.sleep(3)
dc_motor.stop()