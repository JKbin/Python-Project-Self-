import time
# progressbar 설정을 위한 import
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 

# indeterminate : 불확실한 작업을 기다릴 때
# probar = ttk.Progressbar(root, maximum=100, mode="indeterminate")

# determinate : 확실한 작업을 기다릴 때 (ex. 다운로드)
# probar = ttk.Progressbar(root, maximum=100, mode="determinate")
# probar.start(10)    # 10 ms 마다 움직임
# probar.pack()

# def btncmd():
#     probar.stop()   # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

################################

p_var2 = DoubleVar()    # p_var2에 Double 타입의 값을 받는다.
probar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
probar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)    # 0.01초 대기
        
        p_var2.set(i)   # progress bar의 값 설정
        probar2.update()    # ui 업데이트를 위해서
        print(p_var2.get())





btn = Button(root, text="시작", command=btncmd2)
btn.pack()










root.mainloop()

