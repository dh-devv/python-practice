N = int(input())   # 지웅이가 보유한 카드 개수
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

n = N
result = 0
result2 = 0

for d1, d2 in zip(data1, data2):
    if d1 > n and d2 > n:
        break

    if d1 > d2:
        result = N // d1
        N %= d1
    else:
        result = N // d2
        N %= d2
    
    if d1 > n or d2 > n:
        break

    if d1 > d2:
        result2 = n // d2
        n %= d2
    else:
        result2 = n // d1
        n %= d1

print(f"{result} {result2}")