## 파이썬 리스트 함축 및 2차원 리스트 공부 ##


L1 = [i for i in range(80,95,5)]
L2 = [j for j in range(100,90,-4)]
L3 = [e for e in range(70,90,9)]
L = [L1,L2,L3]

for i in l:
    for j in i:
        print(j,end = ' ')
    print()
