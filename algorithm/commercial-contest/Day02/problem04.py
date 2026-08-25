# 4번: 정렬된 자료에서 값 찾기 ( ai 씀 --> 이진 탐색 )

'''
조건: 이진 탐색 방법을 이용하여 구현한다. 근데 이진 탐색을 모름
**이진 탐색(Binary Search)**은 정렬된 데이터에서 원하는 값을 매번 절반씩 버리면서 찾는 알고리즘
'''

잠온다 = list(map(int, input("정렬된 자료 ").split()))
target = int(input("찾을 값 "))

# 이진 탐색
left = 0
right = len(잠온다) - 1

while left <= right :
    mid = (left + right) // 2

    if 잠온다[mid] == target:
        print(f"{mid+1}번째")
        break

    elif 잠온다[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

