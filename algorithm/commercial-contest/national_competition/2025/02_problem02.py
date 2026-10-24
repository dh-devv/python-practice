# 2번 : 파이어 ( FIRE ) 계산기

c = int(input())  # 매월 지출 희망 금액
r = float(input())  # 투자금에 대한 연 수익률 ( 백분율 )

# 매월 지출 희망 금액 x 12 x 연 수익률 x 100

result = (100/r) * (c * 12)

print(int(round(result, -0)))