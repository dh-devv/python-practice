# 파이썬 간단한 학생 점수 관리 프로그램

print("파이썬으로 하는 평균 계산기")   # 제목
score_list = []
print()
print("1000 을 입력한다면 점수 입력을 그만합니다.")  # 무한루프 탈출
total = 0

while True:
    sco = int(input("점수를 입력하세요: "))  # 점수 입력받기
    if sco == 1000:  # 무한루프 탈출하는 경우의 수
        print("프로그램을 종료합니다.")
        break

    # 점수가 1000 이 아닐때 실행된다.
    total += sco  # 점수의 합
    score_list.append(sco)  # 리스트에 점수 넣기

a = len(score_list)  # 리스트에 든 속성 개수

if a == 0:  # 점수가 입력 x 일때
    print("점수를 하나도 입력하지않았으므로 점수와 평균은 출력이 안됩니다.")
else:
    print(f"당신의 점수는 {score_list} 이며, {a} 개의 점수를 입력했습니다.")  # 입력된 점수와 점수의 개수
    print(f"당신의 평균점수는 {total // a} 입니다. ")  # 평균
