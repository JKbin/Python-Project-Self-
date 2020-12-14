# Quiz) tkinter를 이용한 메모장 프로그램을 만드시오.

# [GUI 조건]
# 1. title : 제목 없음 - windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기
import os
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")  # 제목
root.geometry("640x480+450+350" ) # 가로 * 세로 + x좌표 +y좌표

frame = Frame(root)
frame.pack()




###########################################
# 메뉴창
menu = Menu(frame)


file_name = "mynote.txt"
# 열기 함수
def file_open():
    if os.path.isfile(file_name):   # 파일 있으면 True, 없으면 False
        with open(file_name, "r", encoding="utf8") as file:
            txtmain.delete("1.0", END)  # 텍스트 본문 삭제
            txtmain.insert(END, file.read())    # 텍스트에 입력


# 저장 함수
def file_save():
    with open(file_name, "w", encoding="utf8") as file:
        file.write(txtmain.get("1.0",END))  # 모든 내용을 가져와서 저장



menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)  

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

######################################

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 메인 텍스트 박스
txtmain = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set)
txtmain.pack()

scrollbar.config(command=txtmain.yview)



root.mainloop()

