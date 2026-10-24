# 예외 처리 실습하기 


# 이 경우에는 입력을 이상하게 할 경우 print() 가 실행이 안 된다.

'''
int(input("정수 입력: "))
print("반드시 실행돼야 할 문장")
'''


  ## 예외 처리를 사용해 위의 문제를 해결할 수 있다.

try:
    int(input(" 정수 입력: "))

except Exception as e:
    print("정수만 입력하세요")

print("반드시 실행되어야 할 문장")

print('-' * 60)
print()



try:
    print(10 / 0)

except Exception as e:
    print(e.__str__) # 어떤 오류가 나는 지 확인하기

    print("0 으로 나눌 수 없습니다.")