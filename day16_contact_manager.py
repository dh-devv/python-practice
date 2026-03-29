# 파이썬 연락처 관리 프로그램

   
      
 ## 이름, 번호 저장 프로그램 ##
numbers = []  # 번호 저장
names = []  # 이름 저장

print("종료를 입력한다면 저장되며 입력이 끝납니다.")
while True:

    user = input("이름과 전화번호를 입력하세요 ( - 제외 ):  ").split()   # 번호, 이름 묻기

    # 종료하는 방법
    if "종료" in user:
        break

    # 저장되는 방법
    elif len(user) == 2:
        name, number = user
        numbers.append(number)
        names.append(name)
        print("저장 완료")

print()
a = input("확인하시겠습니까? (y/n): ")

# 확인을 할때
if a == 'y':
    print(f"이름: {names}, 번호: {numbers} ")

    print("검색하실 이름을 입력하세요: ")
    n = input()

    for i in names:
        if n == i:
            a = names.index(n)  # 이름에 해당하는 인덱스 번호 찾기
            b = numbers[a]
            print(f"이름: {n}, 번호: {b}")
            break

            # 확인을 안 할때
else:
    print("프로그램이 종료됩니다.")



