# 파이썬 랜덤모듈로 숫자 맞추기 게임 만들기

import random

answer = random.randint(1,50)
count= 0

while True:
  guess = int(input("숫자를 맞춰보세요(1~50):  "))
  count += 1

  if guess > answer:
    print("down")
  elif guess < answer:
    print("up")
  else:
      print(f"정답입니다. 시도횟수: {count}")
      break
