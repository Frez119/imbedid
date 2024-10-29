from gpiozero import Button
from gpiozero import LED
from time import sleep

led = LED(17)
button = Button(27)

# 카운트 변수 초기화
count = 0

while True:
    if button.is_pressed:
        count += 1  # Increase count each time the button is pressed
        print(f"The button has been pressed {count} times.")
        led.on()
    else:
        print("The button is not pressed.")
        led.off()
    sleep(0.2)  # 디바운싱을 위해 대기 시간 줄임
    