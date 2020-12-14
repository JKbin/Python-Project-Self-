from tkinter import *
# combobox를 사용하기 위해서 import 해야함.
import tkinter.ttk as ttk

root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 

cbo_val = [str(i) + "일" for i in range(1,32)]
cbo1 = ttk.Combobox(root, height=5, values=cbo_val)
cbo1.pack()
cbo1.set("카드 결제일") # 최초 목록 제목 설정

# height=10 , 목록을 10개 보여줌
readonlycbo2 = ttk.Combobox(root, height=10, values=cbo_val, state="readonly")   # readonly로 전환
readonlycbo2.current(0) # 0번째 인덱스 값을 디폴트로 설정
readonlycbo2.pack()








def btncmd():
    print("카드 결제일은 :", cbo1.get(), "일입니다.")   # 선택된 값 반환
    print("카드 결제일은 :", readonlycbo2.get(), "일입니다.")   # 선택된 값 반환




btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()

