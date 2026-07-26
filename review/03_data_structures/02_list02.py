# list 실습


#### 문제 ####

'''
1 ~ 100 까지 값 넣고 출력
1 ~ 100 까지 중 짝수만 넣고 출력
A ~ F 까지 넣고 출력
A ~ F 까지 넣고 C 제외하고 출력
a ~ z 까지 넣고 출력
"ABC"에서 B를 Z 로 변경하기
'''

# 1 번 문제

data = [i for i in range(1, 101)]

print(data)

print('-' * 60)

# 2 번 문제

numbers = [i for  i in range(1, 101) if i % 2 == 0]

print(numbers)

print('-' * 60)

# 3 번 문제

String = [i for i in range(65, 71)]

for Str in String:
    print(chr(Str), end= '')

print("\n" + '-' * 60)

# 4 번 문제

# String 은 28번 라인에서 선언함

for Str in String:
    if Str == 67:
        continue

    print(chr(Str),end = '')

print("\n" + "-" * 60)

# 5번 문제

English = [i for i in range(97, 123)]

for En in English:
    print(chr(En), end = '')

print("\n" + "-" * 60)

# 6 번 문제

# English 는 5번 문제에서 선언되었음

String_list = ["A", "B", "C"]

for String in String_list:
    if String == "B":
        index = String_list.index("B")
        String_list[index] = "Z"


print(String_list, end = '')

print("\n" + '-' * 60)