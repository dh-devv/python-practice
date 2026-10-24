# 3번: 최소 동전 개수 구하기  ( ai 사용 )

price = [1, 3, 4] # 사용 가능한 동전의 금액
hope = 6    # 목표 금액

dp = [0]

###    dp 채우기
for i in range(1, hope+1):
    min_coin = 999    # 현재 금액의 최소 동전 개수

    for j in price:
        if i-j < 0:  # 현재 금액보다 동전의 금액이 클 경우
            continue

        result = dp[i - j] + 1

        if result < min_coin:
            min_coin = result

    dp.append(min_coin)
    #new_value = dp[-1] + 1
    #dp.append(new_value)

print(f"최소 동전 개수: {dp[hope]}")


        

    