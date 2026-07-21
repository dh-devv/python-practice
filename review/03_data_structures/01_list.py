data_list = [2 ,4, 5, 6]

print(len(data_list))
print(data_list[2])
print(data_list)

a = data_list
a.append(1)

print(a)
a.remove(2)

print(a)
a.append(1)
a.remove(1)

print(a)

del a[1]
print(a)

a.clear()
print(a)

print('-' * 60)

data = [i for i in range(1, 10)]

print(data.index(4))
data.insert(1, 3)

print(data)