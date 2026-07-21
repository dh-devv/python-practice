
print(chr(ord('A') * 3))
print(chr(ord('A') * 4))
print(chr(ord('A') * 9))

# ord () 로 문자를 숫자로 변경한다.
# chr () 로 숫자를 문자로 변경한다.

print('-' * 60)
password = "a1b2c3"
en_pw = ""
de_pw = ""
for i in password :
    en_pw += chr(ord(i) * 9)  # 암호화하기

print("기존 비밀번호: ", password)
print("암호화된 비밀번호: ", en_pw)

for i in en_pw :
    de_pw += chr(ord(i) // 9)   # 복호화하기

print("복호화된 비밀번호: ", de_pw)

# 결론 : 아스키코드를 통해서 암호화를 할 수 있다.
# pw 또는 개인정보를 암호화할 때, 아스키 코드를 사용한다.
