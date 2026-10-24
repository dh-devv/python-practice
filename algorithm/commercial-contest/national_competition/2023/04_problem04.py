s = input()
string = input()

s1 = s
s2 = 'abcdefghijklnmopqrstuvwxyz'

answer = ''

for i in string:
    if i == ' ':
        answer += i
        continue
    
    index = s2.index(i)

    answer += s1[index]

print(answer)