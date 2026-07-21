# 반복문 !!

# A ~ F 까지 출력하기
#    아스키 코드를 활용해야 함


for i in range(6) : # 0 부터 5까지 1씩 증가함
    print(chr(i + 65))

print()

# A ~ F 까지 중 C 를 제외하고 출력하기

for i in range(6):
    string = i + 65

    if string != 67:
        print(chr(string))
