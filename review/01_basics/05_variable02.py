
name = "변동헌"
age = 17
height = 1000
hobby = "피아노"

print("이름: ", end = '')
print(name)

print()
print("나이: ", end = '')
print(age, end = "살\n")

print()
print("키: ", end = '')
print(height, end = 'cm\n')

print()
print("취미: ", end ='')
print(hobby)

# 위 로직은 복잡하고 가독성이 좋지 않다.

# 서식 문자 ( format )
'''
%d : 정수 ( 10 진수 )
%o : 정수 ( 8 진수 )
%x : 정수 ( 16 진수 )
%f : 실수
%s : 문자열
%c : 문자
'''

print("이름: ", name)
