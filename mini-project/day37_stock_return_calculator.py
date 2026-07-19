## 주식 수익률 계산 프로그램 ##
N = int(input()) # 구매한 주식의 종류

# 변수 선언 #
stock_sum = 0
stock_new_sum = 0
stock_counts = []
stock_names = []
user_input = []
cnt = 0

# 주식 구매 당시 정보 입력 #
while cnt < N:
    try:
        stock_name = input("해당 주식의 이름: ") # 주식 이름
        stock_price = int(input("해당 주식의 가격: ")) # 주식 가격
        stock_count = int(input("해당 주식의 개수: ")) # 주식 개수

    except ValueError:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    if stock_name in stock_names:
        print("이미 입력한 주식 이름입니다. 다시 입력해주세요.")
        continue
    cnt += 1
    stock_counts.append(stock_count)
    stock_names.append(stock_name)

    stock_sum += stock_price * stock_count # 주식 총액
    if stock_sum == 0:
        print("계산 불가")
        exit()

print('-' * 60)
cnt = 0
# 주식 현재 정보 입력 #
while cnt < N:
    try:
        stock_new_name = input("해당 주식의 이름: ") # 주식 이름
        stock_new_price = int(input("해당 주식의 현재 가격: ")) # 주식 현재 가격

    except ValueError:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    if stock_new_name not in stock_names:
        print("입력한 주식 이름이 존재하지 않습니다. 다시 입력해주세요.")
        continue
    else:
        if stock_new_name in user_input:
            print("이미 입력한 주식 이름입니다. 다시 입력해주세요.")
            continue
        cnt += 1
        user_input.append(stock_new_name)

        index = stock_names.index(stock_new_name)
        stock_new_sum += stock_new_price * stock_counts[index] # 주식 현재 총액

# 수익률 계산 #
total = round(( stock_new_sum - stock_sum ) / stock_sum * 100, 2)

# 수익률 출력 #
if total < 0 :
    print(f"수익률은 {total} % 입니다.")
elif total == 0:
    print(f"수익률은 0 % 입니다.")
else:
    print(f"수익률은 {total} % 입니다.")