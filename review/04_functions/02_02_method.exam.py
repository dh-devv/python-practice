# 함수 심화 예제

# 1. 5개의 정수 중 최댓값과 최솟값을 구해주는 메소드

def getMaxAndMin(numbers) :

      # 방법 1
    #max = max(numbers)
    #min = min(numbers)

      # 방법 2
    result_list = []
    max_value = numbers[0]
    min_value = numbers[0]

    for i in range(1, len(numbers)) :
        if max_value < numbers[i] :
            max_value = numbers[i]

        if min_value > numbers[i] :
            min_value = numbers [i]

    result_list.append(max_value)
    result_list.append(min_value)

    #return result_list          # list
    return max_value, min_value  # tuple

data_list = [3, 5, 7, 8]
print(getMaxAndMin(data_list))

print('-' * 60)
print()



# 2. 소문자를 대문자로 수정하는 메소드

def changeToUpper(string):
    result = ""
    for s in string :
        if 97 <= ord(s) <= 122 :
             result += chr(ord(s) - 32)

        else:
            result += s


    return result

user_input = input()
print(changeToUpper(user_input))

print('-' * 60)
print()



# 3. 한글을 정수로 바꿔주는 메소드

def changeToInteger(hangle):
    hangle_org = "공일이삼사오육칠팔구"
    result = ""

    for i in hangle :
        result += str(hangle_org.index(i))

    return int(result)

print(changeToInteger("일공이사") + 1)


# 전역변수 (Global Variable)

result = 0  # 전역 변수

def add(num1, num2 = 0) :
    global result   # global 을 써야 전역 변수를 가져올 수 있다.
    # result -> 이건 그냥 지역 변수라서 전역 변수와 다르다.
    result = num1 + num2

def sub(num1, num2) :
    global result
    result = num1 - num2

add(10)   # result = 10
sub(10, 5)   # result = 5
print(result)

'''

                    전역 변수          |             지역변수
함수 안에서 읽기         가능하다.                     가능하다
함수 안에서 수정    불가능 ( global 쓰면 됨 )         가능하다.

함수 밖에서 읽기       가능                     불가능 ( 선언된 지역에서만 가능 )
함수 밖에서 수정      가능                            불가능
'''   