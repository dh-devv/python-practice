# 4번: 우수 선수 선발
N = int(input()) ; players = []
for i in range(N):
    number, goals, assists, fouls = map(int, input().split())

    players.append(number[goals, assists, fouls])
    
point_list = []
numbers = []

for player in players:
    point = player[0] + player[1]

    numbers.append(player)
    point_list.append(point)

maxPoint = 0

for p in point_list:
    index = point_list.index(p)

    if p > maxPoint:
        maxPoint = p
        
        bestPlayer = numbers[index]

    elif p == maxPoint:
        for i in range(3):
            best = players[bestPlayer][i]

            if players[best] < players[p]:
                maxPoint = players[p]
            elif players[best] > players[p]:
                maxPoint = players[best]

print()
