# 문제 1 : 만 나이
date = list(map(int, input().split('/')))  # 생년월일
now_date = list(map(int, input().split('/'))) # 현재 날짜



if date[1] < now_date[1]:
    age = now_date[0] - date[0] - 1
elif now_date[1] > date[1]:
    age = now_date[0] - date[0]
else:
    if date[2] <= now_date[2]:
        age = now_date[0] - date[0]
    elif date[2] > now_date[2]:
        age = now_date[0] - date[0] - 1

print(age)



