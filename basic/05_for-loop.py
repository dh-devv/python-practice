''' 파이썬 반복문 연습
1."Hello" 5번 출력
2.1부터 10까지 출력
3.입력한 숫자까지 출력 '''

for i in range(5):
  print("Hello")

for i in range(1,11):
  print(i)

num = int(input("Enter a number: "))

for i in range(1,num+1):
  print(i)
