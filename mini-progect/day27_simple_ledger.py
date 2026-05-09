```python
items = [] # 물건 이름 저장
money = [] # 물건 가격 저장
## 입력받은 물건의 이름과 가격을 각각의 리스트에 저장하기 ##
def add_item(item, price):
    items.append(item)
    money.append(price)
    print(f"{item} 추가 완료")
print()

## 입력을 그만 받을 때, 입력받은 물건의 금액을 합산하여 출력하기 ##
def show_total():
    total = sum(money)
    print(f"현재까지의 총 지출은 {total} 원 입니다.")


## 사용자에게 물건의 이름과 가격을 입력받아 함수에 넣기 ##
print("종료하려면 종료를 입력하세요")
while True:
    print()
    name = input("항목을 입력하세요: ")
    if name == "종료":
        break

    cost = int(input("가격을 입력하세요: "))
    add_item(name,cost)
show_total() # 입력을 그만 받을 때, def show_total 함수 실행
```
