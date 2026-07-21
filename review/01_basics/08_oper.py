# 연산자 실습 및 정리

price = int(input("가격: "))
print(int(price * 0.9))  # price != int -- > int () 사용하기

num1 = int(input("정수1: "))
num2 = int(input("정수2: "))

addResult = num1 + num2  # 더하기
subResult = num1 - num2  # 빼기
mulResult = num1 * num2  # 곱하기
divResult = num1 // num2  # 몫 구하기
modResult = num1 % num2  # 나머지 구하기

print("{} + {} = {}".format(num1, num2, addResult))
print("{} - {} = {}".format(num1, num2, subResult))
print("{} * {} = {}".format(num1, num2, mulResult))
print("{} // {} = {}".format(num1, num2, divResult))
print("{} % {} = {}".format(num1, num2, modResult))