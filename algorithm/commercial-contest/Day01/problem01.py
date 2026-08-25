# 1번: 매출액의 합계와 평균

sales = list(map(int, input().split()))  # 입력받기

average = 0  # 평균
sumVal = 0  # 합계
for sale in sales:
    sumVal += sale

average = sumVal / len(sales)

'''
sumVal = sum(sales)
average = sumVal / len(sales)
'''

print(f"합계: {sumVal} / 평균: {average}")