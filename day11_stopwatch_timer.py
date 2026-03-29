# 파이썬 타이머 프로그램 만들기 

import time

print("3초 후 시작합니다.")
for i in range(4,0,-1):
  print(i)
  time.sleep(1)

start = time.time()

input("엔터를 누르면 시간 측정을 종료합니다.")

end = time.time()

print(f"걸린 시간: {end - start} 초 입니다.")
