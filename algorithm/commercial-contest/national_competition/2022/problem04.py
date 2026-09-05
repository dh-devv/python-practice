string = input()

cnt = -1
result = []

for i in range(len(string)):
    if i == ' ':
        continue

    if string[i] == string[cnt]:
        continue
    else:
        result.pop(string[i])