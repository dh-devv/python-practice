# 도구 가져오기
import time as ti
from selenium import webdriver
from selenium.webdriver.common.by import By


# 사이트 주소를 변수로 만들기
crawling_link = 'https://school.busanedu.net/pcs-h/na/ntt/selectNttList.do?mi=669007&bbsId=1030737'

# 웹 페이지 열기
driver = webdriver.Chrome()
driver.get(crawling_link)

ti.sleep(3)

# 지정한 부분의 데이터 수집하기

title = driver.find_element(
    By.XPATH,
    '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[4]/td[2]/a'
).get_attribute("textContent").strip()

day = driver.find_element(
    By.XPATH,
    '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[4]/td[4]'
).get_attribute("textContent").strip()


# 반복문을 활용한 데이터 수집
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[1]/td[2]/a'  # 첫 페이지의 첫 번째 공지사항
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[10]/td[2]/a' # 첫 페이지의 두 번째 공지사항


for i in range(1, 11):   # 하나씩 돌면서 출력하기 
    title = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i) +']/td[2]/a'
    ).get_attribute("textContent").strip()

    print(title)
    print("\n")


# 수집한 데이터 출력하기
'''
print(crawling_link)
print(title)
print(day)
'''
input()
driver.quit()