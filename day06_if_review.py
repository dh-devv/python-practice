# 파이썬 조건문 복습

score = int(input("시험 점수를 입력하세요: "))

# 등급 나누기

if score >= 90:
  grade="A"
elif score >= 80:
  grade="B"
elif score >= 70:
  grade="C"
else:
  grade="재시험"

print("-" * 60 )
print(f"당신의 점수는 {score} 입니다.")
print(f"등급 결과는 {grade} 입니다.")
