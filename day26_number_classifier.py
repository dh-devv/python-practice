## 수를 입력받아서 짝수인지, 홀수인지, 0인지 출력하는 프로그램 ##
def user(u):
    if u == 0:  # 입력받은 값이 0일 때
        print('zero')
    elif u%2 == 0: # 입력받은 값이 짝수일 때
        print("even")
    else:       # 입력받은 값이 홀수일 때
        print('odd')

user_2 = int(input())  # 유저한테 숫자 입력받기
user(user_2)  # def 함수 u 에 입력받은 숫자 넣기
