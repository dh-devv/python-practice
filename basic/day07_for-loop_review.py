# 파이썬 반복문 복습하기 ( for )

#1~20 까지 출력
for i in range(1,21):
  print(i)

#1~20 까지의 수 중에서 짝수만 출력
for i in range(1,21):
  if i%2 == 0:
    print(i)


# 구구단 출력하기

for i in range(2,10):
  for j in range(1,10):
    print(f"{i} x {j} = {i*j}")
  print("-" * 60)
