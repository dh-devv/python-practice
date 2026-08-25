# 3번: 평균 이상인 학생 수

scores = list(map(int, input().split()))

sumVal = 0  # 합계
cnt = 0 # 평균 이상인 학생 수

for score in scores:
    sumVal += score

average = sumVal / len(scores)  # 평균

for i in scores:
    if i >= average:
        cnt += 1

'''
average = sum(scores) / len(scores)
'''

print(f"평균: {average} / 평균 이상 학생 수: {cnt}")