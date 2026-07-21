# 조건문 ! 

num1 = int(input())
num2 = int(input())

# 이름 뒤에 소괄호가 오면 함수이다.


# 조건문의 구조
'''

if ( 조건문 ) :
    (실행문)
elif ( 조건문 ) :
    (실행문)
else:
    (실행문)
    
'''

if num1 > num2 :
    print("큰 값: ", num1)
elif num1 < num2 :
    print("큰 값: ", num2)
else:
    print("두 수는 같습니다.")