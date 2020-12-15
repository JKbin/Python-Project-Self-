from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#
import time
# imgurl 다운로드 시 필요한 lib
import urllib.request



driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
# 검색창 찾기
elem = driver.find_element_by_name("q")
# 검색어 자동입력
elem.send_keys("아메리칸 숏헤어")
# 엔터키 적용
elem.send_keys(Keys.RETURN)

# 검색되는 이미지의 양이 많다면 pause time을 조금 늘려줘야 한다.
SCROLL_PAUSE_TIME = 2

# Get scroll height (스크롤의 높이를 알려줌)
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom(브라우저 끝까지 스크롤을 내리겠다.)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    # 스크롤을 다 내리고 new_height에 새로운 높이를 다시 저장
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # 이미지 끝에는 '결과 더 보기' 버튼이 없으므로 예외처리를 해주지 않으면 에러가 뜬다.
        try:
            # '결과 더 보기' 버튼을 클릭하는 코드
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height








# image download code
# Css의 class요소 (elements : 여러가지) - 1번째 이미지를 선택까지
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        # 로딩 될 때까지 3초 기다리기
        time.sleep(3)
        # 1번째 이미지 class 선택 후 이미지 url을 imgUrl 변수에 저장
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        # url을 이용하여 다운로드 (url주소, 저장 할 파일이름)
        urllib.request.urlretrieve(imgUrl, str(count) +  ".jpg")
        count += 1
    except:
        pass
# 여기까지는 37장밖에 다운이 안된다. 왜냐하면 처음 검색을 했을 때 브라우저에 나오는
# 이미지가 한정되어 있기 때문이다. 모든 이미지를 다운 받을려면 스크롤을 내리면서 다운 + '결과 더보기' 라는
# 버튼도 눌러야 더 많은 이미지들이 검색이 가능하다.
# 브라우저 닫아주는 코드
driver.close()