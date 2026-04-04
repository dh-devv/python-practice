## 최대 공약수를 출력하는 프로그램 ##
# 1. 두 수를 입력받기
a, b = map(int,input().split())

# 세트 만들기
s1 = set()
s2 = set()

# 입력받은 수의 약수 찾기
for i in range(1,a+1):
    if a%i == 0:
        s1.add(i)

for j in range(1,b+1):
    if b%j == 0:
        s2.add(j)

s3 = (s1&s2) # 공약수 찾기
L = list(s3) 
L.sort() # 오름차순으로 정렬하기
# 최대 공약수 출력하
print(f"입력하신 두 수의 최대 공약수는 {L[-1]} 입니다.")
