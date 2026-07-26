# 상속 (Inheritance)

## 1. 상속이란?

기존 클래스(부모 클래스)의 필드와 메서드를 새로운 클래스(자식 클래스)가 물려받아 사용하는 기능이다.

---

## 2. 상속 사용 목적

### 1) 코드 재사용

기존에 만들어진 클래스에서 필요한 기능이 있다면 상속받아 그대로 사용할 수 있다.

### 2) 중복 코드 제거

여러 클래스에서 공통적으로 사용하는 기능들을 부모 클래스에 작성하고,
자식 클래스들이 상속받아 사용한다.

---

## 3. 상속 방법

클래스명 뒤에 소괄호를 작성하고,
괄호 안에 상속받을 부모 클래스명을 작성한다.

예시:
```python
class Parent:
    parent_field = "부모 필드"


class Child(Parent):
    child_field = "자식 필드"
```

Child 클래스는 Parent 클래스의 필드와 메서드를 사용할 수 있다.

---

# 다중 상속 (Multiple Inheritance)

## 1. 다중 상속이란?

하나의 클래스가 여러 부모 클래스로부터 상속받는 것이다.

예시:
```python
class A:
    a_field = "A 필드"


class B:
    b_field = "B 필드"


class C(A, B):
    c_field = "C 필드"
```

C 클래스는 A와 B 클래스의 기능을 모두 사용할 수 있다.

---

# 모호성

## 1. 모호성이란?

다중 상속을 사용할 때 여러 부모 클래스에 같은 이름의 필드나 메서드가 존재하면,
어느 부모 클래스의 기능을 사용할지 판단하기 어려운 문제이다.

예시:
```python
class A:
    value = "A"


class B:
    value = "B"


class C(A, B):
    pass
```

C 클래스에서 value를 호출하면 어떤 부모 클래스의 값을 사용할지 문제가 발생한다.

Python은 MRO(Method Resolution Order) 규칙에 따라
메서드와 필드를 탐색한다.

탐색 순서:

C → A → B → object