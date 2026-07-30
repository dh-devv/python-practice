# 웹에 접속하기 ! 

from selenium import webdriver
import time as ti


# driver = webdriver.Chrome()  # 웹 브라우저 열기

crawling_ling = "https://www.step.or.kr/portal/default/myPage/learnManage/myLearn.page"   # 접속할 사이트의 링크 

driver = webdriver.Chrome()
driver.get(crawling_ling)  # 강의 사이트로 접속이 돔

input("엔터를 누르면 종료됩니다.")
driver.quit()