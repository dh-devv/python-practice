# 파이썬 총 복습하기

#input
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name} 님")

#if         조건문
num= int(input("숫자를 입력하세요: "))

if num > 0:    
  print("양수입니다.")
elif num < 0:
  print("음수입니다.")
else:
  print("0 입니다.")

# for loop    반복문
for i in range(5):    # 5번 반복
  print(i, end=' ')   # i 출력

#nested loop    중첩 반복문
for i in range(3):    # 행
  for j in range(3):    # 열
    print'*', end=' ')    # 별 출력
  print()    # 칸 띄우기
