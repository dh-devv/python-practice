# 반복문 !!!

# break : 반복문을 즉시 탈출한다.
# continue : 아래 문장을 실행하지 않고, 다음 반복을 실행한다.


# 문제 1. 1 ~ 10 까지 중 4까지만 출력하기

for i in range(1, 11):

    if i == 4 :
        break

    print(i)
print('-' * 60) 

# 문제 2. 1 ~ 10 까지 중 4를 제외하고 출력하기

for i in range(1, 11) :

    if i == 4 :
        continue
    print(i)
print('-' * 60)

# 문제 3. 100 ~ 1 까지의 수 중에서 70까지만 출력하기

for i in range(100, 0, -1):
    if i == 69 :
        break
    print(i)
print('-' * 60)

# 문제 4. 1 ~ 100 까짇의 수 중에서 3과 5의 공배수만 출력하기

for i in range(1, 100) :
    if i % 3 == 0 and i % 5 == 0 :
        print(i)
        