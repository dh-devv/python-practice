'''
N = input()  # 영단어 입력

# 각 문자를 8진수 문자열로 변환해서 하나로 합치기
octal_number = ""

for character in N:
    octal_number += format(ord(character), "o")   # 8진수 형태로 N을 저장하기


# 런 렝스 부호화 결과
answer = ""

# 현재 숫자의 반복 횟수
count = 1

# 8진수 문자열을 앞에서부터 확인
for i in range(len(octal_number)):

    # 다음 숫자가 존재하고, 현재 숫자와 같으면 개수 증가
    if (
        i + 1 < len(octal_number)
        and octal_number[i] == octal_number[i + 1]
    ):
        count += 1

    # 다음 숫자가 다르거나 마지막 숫자라면 결과 저장
    else:
        # 숫자 + 반복 횟수 순서
        answer += octal_number[i] + str(count)

        # 다음 숫자를 세기 위해 초기화
        count = 1


# 결과는 숫자로만 이루어져 있으므로 정수로 출력
print(int(answer))
'''


N = input()   # 영단어 입력하기

asCode = ''

for i in N:
    result = oct(ord(i))[2:]  # 8진수로 변환하기
    asCode += str(result)

# print(asCode)

answer = ''

while True:

    for i in asCode:
        cnt = 1
        index = asCode.index(i)

        if index == -1:
            answer += (str(cnt) + i)
            break

        for j in asCode[index+1::]:
            if i == j:
                cnt += 1
            else:
                answer += (str(cnt) + i)
                break
    break

print(answer)