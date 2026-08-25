# 5번: 판매 실적 순위의 지점 찾기

sales_data = list(map(int, input().split()))  # 입력받기

max_sales = sales_data[0]  # 최고 판매 실적
min_sales = sales_data[0]  # 최저 판매 실적


'''
output = []
for sales in sales_data:
    if max_sales < sales:   #  근데 좀 이상한데?
        max_sales = sales

    if min_sales > sales:
        min_sales = sales
'''

sales_data.sort(reverse=True)  # 내림차순 정렬
index = sales_data.index(450)

print(f"판매 실적 450의 순위: {index+1}위")