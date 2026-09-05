N = list(map(int, input().split()))

answer = []
for _ in N:
    result = N[-1] + N[-2]

    answer.append(result)

print(answer)