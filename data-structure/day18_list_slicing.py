## 파이썬 리스트 슬라이싱 연습 ##

# 이름 입력받아서 저장 후 나눠서 출력하기 #

names = []   # 이름 저장소

print("종료를 입력하시면 이름 입력이 종료됩니다.")   # 무한루프 탈출방법
while True:
    name = input("당신의 이름을 입력하세요: ")
    if "종료" in name:
        break
    else:
        names.append(name)   # 저장소에 저장

print(f"저장완료: {names}")
print()
print(f"상위 3명: {names[:3]}")  # 상위 3명 출력
print(f"하위 2명: {names[-2:]}")   # 하위 2명 출력
