## 파이썬 2차원 리스트 공부 ##

scores = [[70,80,90],[60,75,85],[100,90,95]]

print(scores[1][2])

for i in range(len(scores)):
    print(f"{i+1},첫번째: {scores[i][0]} / 두번째: {scores[i][1]} / 세번쨰: {scores[i][2]}")

print()
print(scores[2][0])
