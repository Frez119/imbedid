 from gpiozero import Motor
 from time import sleep
 motor = Motor(forward=6, backward=12)

 while True:
    motor.forward()
    sleep(1)
    motor.stop()
    sleep(3)
    motor.backward()
    sleep(1)
    motor.stop()
    sleep(3)

    