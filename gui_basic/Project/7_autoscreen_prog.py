import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageGrab
import time
import keyboard

root = Tk()
root.title("GUI made by JBin")  # 제목


def start_prog():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))   # image_20201215_143220.png ~ 


def stop_prog():
    pass
    





# 멈춤, 시작 프레임
stop_start_frame = Frame(root)
stop_start_frame.pack(fill="x", padx=5, pady=5)

btn_start = Button(stop_start_frame, padx=5, pady=5, width=12, text="시작", command=start_prog)
btn_start.pack(side="right")

btn_stop = Button(stop_start_frame, padx=5, pady=5, width=12, text="멈춤", command=stop_prog)
btn_stop.pack(side="left")


# 메인 이미지 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 종료 프레임
quit_frame = Frame(root)
quit_frame.pack(fill="x", padx=5, pady=5)

btn_quit = Button(quit_frame, padx=5, pady=5, width=12, text="프로그램종료", command=root.quit)
btn_quit.pack(side="right")




















root.resizable(False, False)
root.mainloop()