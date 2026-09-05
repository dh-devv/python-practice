# 1번: 진수 변환

n = int(input())
k = int(input())

answer = []

for _ in range(n):
    if n < k:
        answer.append(n)
        break

    result = n % k
    n //= k

    answer.append(result)

returnVal = answer[::]
val1 = answer[1]
val2 = answer[0]

value = str(val1) + str(val2)
print(value)