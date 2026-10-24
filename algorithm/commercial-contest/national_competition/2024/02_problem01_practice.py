n = int(input())  # 10 진수의 수
k = int(input())  # 희망하는 진수

answer = ''
N = n

while True:
    if N < k:
        answer += str(N)
        break

    result = N % k
    N //= k

    answer += str(result)

answer = answer[::-1]

print(answer)