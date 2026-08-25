# 2번: 매출액의 내림차순 정렬

store = list(map(int, input().split()))
store.sort(reverse=True)

print(*store)  # 내림차순 정렬