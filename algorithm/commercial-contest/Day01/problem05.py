# 5번: 최고 매출 지점 찾기 ( ai 씀 )

user_input = input()

# '/' 기준으로 3개 지점 분리
branch1, branch2, branch3 = user_input.split('/')

school = [branch1, branch2, branch3]

Store = []
Sales = []

# 지점별 매출액 저장
for i in school:
    branch_name, sales = i.split(':')

    Store.append(branch_name)

    # 매출액을 공백 기준으로 분리
    score_list = sales.split(' ')

    for j in score_list:
        if j != '':
            Sales.append(int(j))

    Store.append(Sales)

    # 다음 지점을 위해 초기화
    Sales = []


# 각 지점의 총매출 계산
total_sales = []

for i in range(0, 6, 2):
    total = sum(Store[i + 1])
    total_sales.append(total)

    print(f"{Store[i]} 총매출: {total}", end=' / ')


# 총매출이 가장 높은 지점
max_sales = max(total_sales)
max_index = total_sales.index(max_sales)

print(f"최고 매출 지점: {Store[max_index * 2]}")