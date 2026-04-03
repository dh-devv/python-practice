## 좌석 예약 프로그램 ##
seats = [[0, 0, 0, 0, 0] for i in range(5)]

# 1. 예약할 좌석 번호를 물어보기
print("-1 을 입력하면 프로그램을 종료합니다.")
while True:

    row = int(input("좌석의 행 번호를 입력하세요: "))
    col = int(input("좌석의 열 번호를 입력하세요: "))

    # 2. -1 입력시 좌석 번호 그만 물어보기
    if row == -1 or col == -1:
        print("프로그램을 종료합니다.")
        break

    row_idx = row - 1
    col_idx = col - 1

    # 3. 이미 예약된 자리일 경우
    if seats[row_idx][col_idx] == 1:
        print("이미 예약된 자리입니다.")
        print()

    # 4. 예약이 안된 자리를 골랐을 경우
    else:
        seats[row_idx][col_idx] = 1
        print("예약 성공!")
    print()

print()
# 프로그램을 종료
print("좌석 예약 프로그램을 종료합니다.")
