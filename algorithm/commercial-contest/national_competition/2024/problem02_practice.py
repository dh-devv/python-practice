N = input()  # 영단어 입력
answer = ''

for i in N:
    result = oct(ord(i))[2:]
    answer += result

# print(answer)

returnNUM = ''

while True:

    for i in answer:
        cnt = 1
        index = answer.index(i)

        if index == -1:
            returnNUM += (str(cnt)+ i)
            break

        for j in answer[index+1::]:

            if i == j:
                cnt += 1
            else:
                returnNUM += (str(cnt) + i)
                break
    break

print(returnNUM)