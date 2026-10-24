# 3번 : 베스트셀러
N = int(input()); title_list = []
for i in range(N):
    title = input() # 책 제목
    title_list.append(title)

title_list.sort()
cnt_dict = dict()

for i in title_list:
    if i in cnt_dict.keys():
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

maxVal = 0
minVal = 0
book_name = ''

for key, value in cnt_dict.items():
    if value > maxVal:
        maxVal = value
        book_name = key

print(book_name)