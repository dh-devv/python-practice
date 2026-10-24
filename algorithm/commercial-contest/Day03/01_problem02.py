# 2번: 연결된 지점 모두 방문하기

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    6: [7]
}

result = [1]  # 방문 순서를 저장
visited = [0, 0, 0, 0, 0, 0, 0, 0]  # 방문 여부

stack = [1]  # DFS에 사용할 스택
visited[1] = 1  # 1번 지점 방문

while stack:
    current = stack.pop()

    # 현재 지점과 연결된 지점을 확인
    for next_node in reversed(graph.get(current, [])):

        # 아직 방문하지 않은 지점이면
        if visited[next_node] == 0:
            visited[next_node] = 1
            result.append(next_node)
            stack.append(next_node)

print(*result)