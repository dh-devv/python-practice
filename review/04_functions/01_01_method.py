# 메소드 연습

# f(x) = 2x + 1

def f(x) :
    return 2 * x + 1

print(f(3) + 9)



# 두 정수의 덧셈

def add(num1, num2) :
    result = num1 + num2

    return result

print(add(3 ,5))


# 1 ~ 100 까지 print() 로 출력하는 메소드
def printFrom1To100() :
    for i in range(1, 101) :
        print(i, end=' ')

printFrom1To100()


# 1 ~ 10 까지의 합을 구하는 메소드
def sumFrom1To10():
    result = 0
    for i in range(1, 11):
        result += i

    return result

print("\n", sumFrom1To10())


# 자연수를 음수로 바꿔주는 메소드
def changeToNegative(num):
    result = 0

    if num > 0:
        result = num * -1
    else:
        result = False

    return result 

result = changeToNegative(int(input("자연수: ")))

if not result :
    print("자연수만 가능합니다.")
else:
    print(result)


# 1 ~ n 까지의 print() 로 출력하는 메소드
def printsumFrom1(end):
    result = 0

    for i in range(1, end+1):
        result += i
    print(result)

printsumFrom1(10)


# 짝수를 홀수로, 홀수를 짝수로 바꾸는 메소드
def change(num) :
    if num > -1 :
        num += 1
    else:
        num = False

    return num

num = int(input("정수: "))
result = change(num)

if not result :
    print("양수만 가능해요")
else:

    if result % 2 == 0:
        print("홀 -->  짝")
    else:
        print("짝 -->  홀")


# 5개의 정수를 오름차순으로 정렬해주는 메소드
def sortASC(numList):
    numList.sort()

    return numList
numList = [9, 7, 3, 1, 2]

print(sortASC(numList))