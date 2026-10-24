## 크롬 드라이버 확인하기

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")  

input("엔터를 누르면 종료됩니다.")
driver.quit()