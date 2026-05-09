#if - else practice with input

n = int(input("정수를 하나 입력하세요: "))

if n < 0:
  print(f"{n} 은 음의 정수입니다.")
elif n > 0:
  print(f"{n} 은 양의 정수입니다.")
else:
  print(f"{n} 은 0 입니다.")
