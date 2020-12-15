import time
from PIL import ImageGrab
# pip install keyboard
import keyboard 

def screenshot():
    # 2020년 12울 15일 14시 32분 20초 > 20201215_143220
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))   # image_20201215_143220.png ~ 

keyboard.add_hotkey("F9", screenshot)   # 사용자가 F9를 누르면 실행
keyboard.wait("esc")    # 사용자가 esc를 누르면 프로그램 종료














#time.sleep(5)   # 사용자가 준비하는 시간 : 5초
# for i in range(1,11): # 2초 간격으로 10개 이미지 저장
#     img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
#     img.save("image{}.png".format(i))   # 파일로 저장(image1.png ~ image10.png)
#     time.sleep(2)

    
