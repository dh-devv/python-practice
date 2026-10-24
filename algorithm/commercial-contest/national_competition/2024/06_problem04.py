# 4번: 공약수의 합

A, B = map(int, input().split())

total = 0
if A > B:
    for i in range(1, B+1):
        if B % i == 0 and A % i == 0:
            total += i

elif A < B:
    for i in range(1, A+1):
        if A % i == 0 and B % i == 0:
            total += i

else:
    for i in range(1, A+1):
            if A % i == 0 and B % i == 0:
                total += i

print(total)