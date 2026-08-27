# 2번: 계단 오르기 경우의 수

n = int(input()) # --> 올라갈 계단의 개수

dp = [1, 1]  # 계단을 올라가는 경우의 수를 인덱스로 저장하기

'''
def 경우의수(number):
    cnt = 0  # 경우의 수 초기화
    for i in range(number):
        for j in range(number):
            if i > 2 or j > 2:   # 오르는 계단 수 제한
                continue
            elif i + j == number:
                cnt += 1  # 해당 목표에 도달하는 경우의 수

    return cnt
'''

for i in range(2, n+1):
    new_value = dp[-1] + dp[-2]  # 마지막과 그 앞의 경우의 수 더하기
    dp.append(new_value)

    #dp.append(dp[-1] + 경우의수(i))

print(dp[-1])

