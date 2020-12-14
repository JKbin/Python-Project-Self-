from tkinter import *

root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 


label1 = Label(root, text="메뉴를 선택하세요")
label1.pack()

burger_var = IntVar()   # burger_var에 int형응로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="빅맥", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="상하이버거", value=2, variable=burger_var)
# btn_burger2.select()    
btn_burger3 = Radiobutton(root, text="더블불고기버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


label2 = Label(root, text="음료를 선택하세요")

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()










def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)를 반환
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 값(value)를 반환




btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop()

