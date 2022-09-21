import heapq

T = int(input())
INF = float('INF')
d_i = [1, -1, 0, 0]
d_j = [0, 0, 1, -1]

for tc in range(1, T+1):
    N = int(input())
    if not N: break
    cave = []
    for _ in range(N):
        cave.append(list(map(int, input().split())))
    distance = [[INF for _ in range(N)] for _ in range(N)]

    def dijkstra():
        distance[0][0] = cave[0][0]
        queue = [(cave[0][0], 0, 0)]

        while queue:
            dist, now_i, now_j = heapq.heappop(queue)
            if distance[now_i][now_j] < dist:
                continue

            for i in range(4):
                next_i = now_i + d_i[i]
                next_j = now_j + d_j[i]
                if 0 <= next_i < N and 0 <= next_j < N:
                    tmp = dist + cave[next_i][next_j]
                    if tmp < distance[next_i][next_j]:
                        distance[next_i][next_j] = tmp
                        heapq.heappush(queue, (tmp, next_i, next_j))
    
    dijkstra()
    print('#{} {}'.format(tc, distance[N-1][N-1]))
    tc += 1