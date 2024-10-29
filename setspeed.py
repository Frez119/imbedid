from gpiozero import Robot
import time
from tkinter import *

dc_motor = Robot(left=(6, 12), right=(11, 9))

def control_speed(val):
    speed = float(val)
    if current_direction.get() == "forward":
        dc_motor.forward(speed=speed)
    elif current_direction.get() == "backward":
        dc_motor.backward(speed=speed)

def set_forward():
    current_direction.set("forward")
    dc_motor.forward(speed=float(speed_scale.get()))

def set_backward():
    current_direction.set("backward")
    dc_motor.backward(speed=float(speed_scale.get()))

def stop_motor():
    dc_motor.stop()

# GUI 설정
root = Tk()
root.title("DC 모터 속도 제어")

current_direction = StringVar(value="stop")

# 속도 조절 슬라이더
speed_scale = Scale(root, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, 
                   label="속도 조절", length=200, command=control_speed)
speed_scale.set(0.5)
speed_scale.pack(pady=10)

# 방향 제어 버튼
Button(root, text="전진", command=set_forward).pack(pady=5)
Button(root, text="후진", command=set_backward).pack(pady=5)
Button(root, text="정지", command=stop_motor).pack(pady=5)

root.mainloop()