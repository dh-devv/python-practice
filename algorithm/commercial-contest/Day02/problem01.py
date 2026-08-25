# 1번: 점수를 오름차순으로 정렬하기 ( ai 씀 )

scores = list(map(int, input().split()))  # 입력받기

# 조건: 반복문을 이용한 정렬

for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] > scores[j]:
            scores[i], scores[j] = scores[j], scores[i]

print(*scores)