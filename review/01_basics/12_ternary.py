
# 퀴즈 게임 

Msg = "다음 중 프로그래밍 언어가 아닌 것은?"
choicMsg = " 1. java\n 2. python\n 3. c\n 4. 망둥어\n"
choice = int(input(Msg + "\n" + choicMsg))
answer = 4

#result = "정답" if choice == answer else "오답..."
result = (("정답" if choice == answer else "오답.."
            if choice >= 1 and choice <= 4 
            else "잘못 입력하셨습니다."))


 # 삼항 연산자를 여러 번 쓰면 가독성이 떨어진다는 단점이 있다. #
print(result)