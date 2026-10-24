## CodeUp 1805: 입체기동장치 생산공장 문제

n = int(input())
record = {}

for i in range(n):
    number, gas = map(int, input().split())

    if 1 <= number <= 100 and 0 <= gas <= 10000:
    
        if number in record:
            print("이미 입력된 값입니다.")
            break
        
        record[number] = gas
    

for key, value in sorted(record.items()):
    print(f"{key} {value}")
