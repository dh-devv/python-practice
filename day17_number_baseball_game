## 파이썬으로 만든 야구 게임 ##

import random as rd

Strike = 0
ball = 0
c_numbers = []
u_numbers = []

# 1. 컴퓨터 숫자 정하기
while len(c_numbers) < 3:
    num = rd.randint(1, 9)
    if num not in c_numbers:
        c_numbers.append(num)

# 컴퓨터가 정한 수
# print(f"컴퓨터 숫자: {c_numbers}")

# 2. 유저한테 입력 받기
user_input = input("숫자 3개를 입력하세요(띄워쓰기로 구분한다): ").split()
us1 = user_input[0]
us2 = user_input[1]
us3 = user_input[2]

if us1 == us2 or us2 == us3 or us1 == us3:
    print("중복된 수를 입력하셨습니다.")
else:
    # 문자열을 숫자로 바꿔서 저장
    u_numbers.append(int(us1))
    u_numbers.append(int(us2))
    u_numbers.append(int(us3))

    # 스트라이크랑 볼 구분하기
    for i in range(3):  # 유저 숫자의 위치 (0, 1, 2)
        for j in range(3):  # 컴퓨터 숫자의 위치 (0, 1, 2)
            if u_numbers[i] == c_numbers[j]:  # 숫자가 같을 때
                if i == j:  # 위치까지 같으면
                    Strike += 1
                else:  # 위치는 다르면
                    ball += 1

    if Strike == 3:
        print("정답입니다.")

print(f"스트라이크: {Strike}, 볼: {ball}")
