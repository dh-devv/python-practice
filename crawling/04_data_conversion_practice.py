# 데이터 변환 연습

import time as ti
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

crawling_link = 'https://school.busanedu.net/pcs-h/na/ntt/selectNttList.do?mi=669007&bbsId=1030737'


driver = webdriver.Chrome()
driver.get(crawling_link)

ti.sleep(3)

'''
# 공지사항 제목
for i in range(1, 11):   # 하나씩 돌면서 출력하기 
    title = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i) +']/td[2]/a'
    ).get_attribute("textContent").strip()

    print(title)
    print("\n")


#작성자
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[1]/td[3]'
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[10]/td[3]'

for i in range(1, 11):
    name = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[3]'
    ).get_attribute("textContent").strip()

    print(name)
    print("\n")

# 등록일

'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[1]/td[4]'
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[10]/td[4]'

for i in range(1, 11):
    day = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[4]'
    ).get_attribute("textContent").strip()

    print(day)
    print("\n")

# 조회
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[1]/td[5]'
'//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr[10]/td[5]'

for i in range(1, 11):
    view = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[5]'
    ).get_attribute("textContent").strip()

    print(view)
    print("\n")
'''
    # 이러면 보기도 힘들고 비효율적임 


# 데이터를 저장할 공간
title_list = []
name_list = []
date_list = []
view_list = []

# 하나의 반복문으로 가독성 높이기
for i in range(1, 11):

    title = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[2]/a'
    ).get_attribute("textContent").strip()

    name = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[3]'
        ).get_attribute("textContent").strip()

    date = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[4]'
        ).get_attribute("textContent").strip()

    view = driver.find_element(
        By.XPATH,
        '//*[@id="subContent"]/div/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[5]'
        ).get_attribute("textContent").strip()

         # 저장하기
    title_list.append(title)
    name_list.append(name)
    date_list.append(date)
    view_list.append(view)

    '''
       # 출력하기
    print(title)
    print(name)
    print(date)
    print(view)

    print("-" * 60)
    print()

    '''

#print(title_list)
#print(name_list)
data = pd.DataFrame(data={'제목': title_list, '작성자': name_list,
              '날쨔': date_list, '조회 수': view_list})

data.to_excel('result.xlsx', index = False)
print(data)
input()
driver.quit()