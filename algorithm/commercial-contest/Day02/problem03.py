# 3번: 상품 번호 찾기

numbers = list(map(int, input("상품 번호 ").split()))
findNum = int(input("찾을 번호 "))

index = numbers.index(findNum)

print(f"{index+1}번째")