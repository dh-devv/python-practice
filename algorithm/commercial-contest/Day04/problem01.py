#  1번: 피보나치 수 구하기 ( 동적계획법 )

# 동적계획법이란?
#   큰 문제를 작은 부분 문제로 나누어 푼 뒤, 그 결과를 저장해 재사용함으로써 전체 문제를 효율적으로 해결하는 알고리즘 설계 기법


n = int(input())  # n번째 피보나치 수 출력해야해서 입력받기
result = [1,1]  # 구한 값 저장하기


for _ in range(n-2):

    new_value = result[-1] + result[-2]  # 마지막 값과 그 앞의 값 더하기
    result.append(new_value) 

    '''
    if (i+1) == n:
        result.append(result[i] + (i))
    else:
        result.append(result[i] + (i+1))  # i번째 피보나치 저장하기
    '''

print(result[-1])