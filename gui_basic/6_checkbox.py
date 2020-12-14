from tkinter import *

root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 

chkvar = IntVar()   # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 디폴트로 선택되어 있음
# chkbox.deselect()   # 디폴트로 선택 안되어 있음
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()







def btncmd():
    print(chkvar.get()) # 0 : 체크 x, 1: 체크 o
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()

