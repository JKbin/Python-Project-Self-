from tkinter import *

root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 


txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

# Entry : 한 줄만 사용할 때
e = Entry(root, width=30)
e.pack()
e.insert(END, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 첫번째 라인, 0 : 0번째 컬럼 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()

