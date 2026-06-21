## 딕셔너리 복습 ##

students = {
    "name": "동헌",
    "grade": 1,
    "class": 2
}

# 출력
print(students["name"])
print(students["grade"])

# 새로운 딕셔너리 생성
students2 = {
    "name": "홍길동",
    "grade": 2,
    "class": 3
}


# 출력
print(students2["name"])
print(students2["grade"])


# 값 추가
students["score"] = 100
students["score"] = 90

# 값 삭제
del students["grade"]

# 값 수정
students["grade"] = 2


# 출력

print("학생 1")
print(students)
print()

print("학생 2")
print(students2)
print()

# 반복문을 통해서 출력하기

for key in students:
    print(key, students[key])