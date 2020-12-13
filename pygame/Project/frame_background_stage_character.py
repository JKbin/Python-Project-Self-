import pygame
import os
############################################################
# 기본 초기화 (반드시 해야함)
pygame.init() 

# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Making PangGame by JBin") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)


# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)    # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images")   # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)      # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height - stage_height        



# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6




# 폰트 정의
game_font = pygame.font.Font(None, 40)      # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()       # 시작 tick을 받아옴




############################################################


# 이벤트 루프(창이 꺼지지 않도록)
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)                 # 게임화면의 초당 프레임 수를 설정
    # 2. 이벤트 처리 (키보드, 마우스 등)
   
                
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표사

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False
   
    
    pygame.display.update()             # 게임화면 다시 그리기!

# 잠시 대기
#pygame.time.delay(2000)     # 2초 정도 대기



# pygame 종료
pygame.quit()

