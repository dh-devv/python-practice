## 예외 처리 연습하기 ##


print("<< 두 수를 나누는 프로그램 >>")
while True:
    try:
        num1, num2 = map(int, input("숫자를 입력해주세요 ( a / b ): ").split('/'))
        result = num1 / num2

    except ZeroDivisionError:
        print(" 0 을 제외한 수를 입력해주세요")
        print('-' * 60)
        print()

    except ValueError:
        print(" 수를 입력해주세요 ")
        print('-' * 60)
        print()

    else:
        print("제대로 입력을 하셨습니다.")
        print()

        print(round(result, 2))
        print(" (( 계산 완료 )) ")

        break

print("프로그램을 종료합니다.")
    