def solution(arr1, arr2):
    answer = 0
    one = 0
    two = 0
    
    if len(arr1) != len(arr2):  # 첫 번째, 조건
        if len(arr1) > len(arr2):
            answer = 1
        else:
            answer = -1
    else:                       # 두 번째, 조건
        for i in range(len(arr1)):
            one += arr1[i]
            two += arr2[i]
            
            if one == two:
                answer = 0
            elif one > two:
                answer = 1
            elif one < two:
                answer = -1
    
    return answer