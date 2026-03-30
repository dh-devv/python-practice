## 일정 정리 프로그램 ##
takes = [] # 일정을 저장할 공간
print("종료를 입력하면 할 일을 그만 입력합니다")

# 1. 일정을 입력받기
while True:
    take = input("할 일을 입력하세요: ")

    # 일정을 그만 입력받기
    if take == ('종료'):
        break
    # 일정 저장
    else:
        takes.append(take)
print()
print("저장완료, 목록을 보시겠습니까? y/n ")
a = input()

# 일정 목록 보기
if a == 'y':
    print(f"목록: {takes}")
print()
print("삭제: 1, 추가: 2, 보기: 3 을 입력해주세요: ")


print()
print("종료 입력시 수정이 종료됩니다.")
while True:
    user = input()

    if user == '종료':
        break
    # 일정 삭제 #
    if user == '1':
        u = input("삭제할 일을 입력하세요: ")
        for i in range(len(takes)):
            if takes[i] == u:
                takes.pop(i)
                print(f" 수정 완료된 일정: {takes}")

    # 일정 추가 #
    elif user == '2':
        us = input("추가할 일을 입력하세요: ")
        takes.append(us)
        print(f" 수정 완료된 일정: {takes}")


    # 일정 보기 #
    elif user == '3':
        print(f"{takes}")

    else:
        print("프로그램을 종료합니다.")
