# 1번: 총점과 평균점수 구하기

N = int(input())  # 과목의 수
Scores = list(map(float, input().split()))   # 과목별 점수 입력

average = round(sum(Scores) / len(Scores), 1)

print(sum(Scores))
print(average)