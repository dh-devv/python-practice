# 2번: 토끼의 번식

N = int(input()); date = [1, 1]
for i in range(N-1):

    result = date[-1] + date[-2]
    date.append(result)

print(date[-1])