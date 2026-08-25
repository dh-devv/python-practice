# 2번: 최고 점수와 최저 점수

numbers = list(map(int, input().split()))

maxVal = 0  # 최고 점수
minVal = numbers[0]  # 최저 점수

for number in numbers:
    if maxVal < number:
        maxVal = number

    if minVal > number:
        minVal = number

'''
maxVal = max(numbers)
minVal = min(numbers)
'''
print(f"최고 점수: {maxVal} / 최저 점수: {minVal}")