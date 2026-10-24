
def gcd(a, b): # 최대 공약수를 구하는 함수
    a_num = []
    b_num = []

    for i in range(1, a + 1):
        if a % i == 0 :
            a_num.append(i)
        else:
            continue
    
    for j in range(1, b + 1):
        if b % i == 0 :
            b_num.append(j)

    common = list(set(a_num) & set(b_num))

    return max(common)

def lcm(a, b):  # 최소 공배수를 구하는 함수
    return (a * b) // gcd(a, b)

def factorial(n):   # 팩토리얼을 구하는 함수
    total = 1

    for i in range(n, 0, -1):
        total *= i

    return total

def is_prime(n):  # 소수임을 판단하는 함수
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        else:
            continue
    
    if cnt == 2:
        return True
    else:
        return False

