from tkinter import *


root = Tk()
root.title("GUI made by JBin")  
root.geometry("640x480+450+300" ) 

def create_new_file():
    print("새 파일 만들기")


menu1 = Menu(root)

# File 메뉴
menu_file = Menu(menu1, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")    # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu1.add_cascade(label="File", menu=menu_file)


# Edit 메뉴 (빈 값)
menu1.add_cascade(label="Edit")

# Language 메뉴 추가 (radiobutton을 통해서 선택 1 가능)
menu_lang = Menu(menu1, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C#")
menu1.add_cascade(label="Language", menu=menu_lang)


# View 메뉴(checkbutton)
menu_view = Menu(menu1, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu1.add_cascade(label="View", menu=menu_view)


root.config(menu=menu1)











root.mainloop()

