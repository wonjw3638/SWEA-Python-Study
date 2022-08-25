# 5102_노드의 거리
# 2022-08-25

# bfs 구현 함수
def bfs():
    global queue
    # 중복 검사 및 거리 저장
    visited = [0] * (V+1)

    # 모든 경로 확인
    while queue:
        item = queue.pop(0)
        # 방문한 적 없으면 방문 처리
        if visited[item[0]] == 0:
            visited[item[0]] = item[1]

        # 해당 노드에서 갈 수 있는 간선 탐색
        for i in edges[item[0]]:
            # 방문한적 없는 노드와 연결되어 있을 경우
            if visited[i] == 0:
                queue.append((i, item[1]+1))
    # 최종 값 리턴
    return visited[G]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)
        edges[v2].append(v1)
    S, G = map(int, input().split())

    queue = list()
    for s in edges[S]:
        queue.append((s, 1))

    result = bfs()
    print('#{} {}'.format(tc, result))