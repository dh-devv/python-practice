
  #  나만의 예외 만들기
class NickNameError(Exception):
    pass

def checkNickName(name):
    if name == "바보" :
        raise NickNameError

nickname = input("닉네임: ")

try:
    checkNickName(nickname)
    print("닉네임 생성 성공")

except NickNameError as e :
    print("비속어는 사용할 수 없어요")


print('-' * 60)
print()

'''
외부에서 래팅 문자열을 받아와서 in 으로 검사한다.
비속어는 바보, 멍청이, 똥개이다.
사용자 예외 처리로 만들며, 비속어가 없다면 메세지를 출력한다
'''

class BadWordError(Exception):  # 나쁜 말 에러 만들기
    pass

chat = ""

def checkChatting(temp) :
    badwords = ["바보", "멍청이", "똥개"]  # 나쁜말 목록

    for word in badwords: 
        if word in temp:   # 채팅에 나쁜 말이 있다면?
            global chat

            chat = temp.replace(word, "*")  # 검열하기
            raise BadWordError()

cnt = 0
while True:
    chat = input("채팅[나가기: q]")

    if chat.lower() == 'q':
        break

    try:
        checkChatting(chat)

    except BadWordError:
        cnt += 1

        print(f" {cnt} 회 비속어를 사용하셨습니다.")
        print( chat)