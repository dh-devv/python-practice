# 삼항 연산자

# 참 if 조건식 else 거짓

# 예시
print(10 if 10 > 1 else 1)

# 풀이
'''
10 > 1 이라는 가운데 조건식이 참이라서
  10 이 됨
반대로 거짓이라면 1 이 된다.
'''

num1 = int(input("첫 번째 수: "))
num2 = int(input("두 번쨰 수: "))

# num1 이 num2 보다 크면 True
# num1 이 num2 보다 작으면 False
# num1 과 num2 가 같아도 False
result = num1 if num1 > num2 else "X\n 두 수가 같습니다." if num1 == num2 else num2


print("더 큰 값: ", result)

# 연산과 연결

print(10 + 9)  # 연산
print('10' + '9') # 연결
# print('10' + 9)  # 에러가 뜸

