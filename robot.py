from gpiozero import Motor, Robot
from time import sleep
import tkinter as tk
from tkinter import ttk

# GUI 윈도우 생성
window = tk.Tk()
window.title("MOTOR speed control")
window.geometry("300x200")

# 모터 초기화
motor = Motor(forward=6, backward=12)
dc_motor = Robot(left=(6, 12), right=(11, 9))

# 속도 제어 함수
def control_speed(value):
    speed = float(value)
    dc_motor.forward(speed=speed)

# 스케일 위젯 생성
speed_scale = ttk.Scale(
    window,
    from_=0,
    to=1,
    orient='vertical',
    length=150,
    command=control_speed
)
speed_scale.set(0)  # 초기값 설정
speed_scale.pack(pady=20)

# 정지 버튼 함수
def stop_motor():
    dc_motor.stop()
    speed_scale.set(0)

# 정지 버튼 생성
stop_button = ttk.Button(window, text="정지", command=stop_motor)
stop_button.pack()

window.mainloop()
