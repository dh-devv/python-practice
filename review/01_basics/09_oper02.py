# 연산자 2

# 관계연산자
'''
== : 같다.
!= : 같지 않다.
'''

isTrue = 10 == 11
isTrue = 10 != 11

print(isTrue)

# 논리 연산자
'''
and
or
not
'''
isTrue = 10 == 11 and 10 > 1
isTrue = 10 == 11 or 10 > 1
print(isTrue)

# 비트 연산자  ( 비트 : 0 또는 1 )
'''
& ( and ) : 두 비트가 모두 1이면 1
| ( or)  : 둘 중 하나라도 1이면 1
^ ( xor )  : 두 비트가 서로 다르면 1
'''

print(10&11)  # 1010 과 1011
print(10|11)
print(10^11)

'''
~ (not) : 0을 1로, 1을 0으로 
'''

print(~10)  # -11

