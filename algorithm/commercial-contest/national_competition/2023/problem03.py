# 3번 : 진수 변환기

N = int(input())  # 10진수의 숫자

b = ''
n = N

while True:
    if N < 2:
        if N == 0:
            b += '0'
        elif N == 1:
            b += '1'

        break

    result = N % 2
    N //= 2

    b += str(result)

#print(b) 1100011

t = ''
N = n

while True:
    if N < 3:
        if N == 0:
             t += '0'
        elif N == 1:
            t += '1'
        elif N == 2:
            t += '2'
        break

    result = N % 3
    N //= 3

    t += str(result)

#print(t)  0020

f = ''
N = n

while True:
    if N < 4:
        if N == 0:
            f += '0'
        elif N == 1:
            f += '1'
        elif N == 2:
            f += '2'
        elif N == 3:
            f += '3'
        break

    result = N % 4
    N //= 4

    f += str(result)

#print(f) 3021

B = b[::-1]
T = t[::-1]
F = f[::-1]

print(B)
print(T)
print(F)