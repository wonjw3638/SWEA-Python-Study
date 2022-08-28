# 1226_미로1
# 220826
'''
설계 5
구현 18:05 ~ 
'''

import sys
sys.stdin = open('input.txt','rt')

# 델타 구현
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def maze(map_list, s):
    # 큐를 최대 길이로 설정
    queue = [0] * (16**2)
    rear = front = -1

    # 시작 노드 체크
    v = s
    visited[v[0]][v[1]] = 1
    rear += 1
    queue[rear] = v

    while front < rear:
        front += 1
        v = queue[front]
        # 방문하지 않은 노드
        for d in range(4):

            w = [v[0] + di[d], v[1] + dj[d]]

            # 갈 수 있는 길인 경우
            if map_list[w[0]][w[1]] == '0':
                if visited[w[0]][w[1]] == 0:
                    rear += 1
                    queue[rear] = w
                    visited[w[0]][w[1]] = 1
                else:
                    continue
            # 도착점인 경우
            elif map_list[w[0]][w[1]] == '3':
                return 1
            else:
                continue

    return 0


for _ in range(10):
    tc = int(input())
    map_list = list()

    for i in range(16):
        map_input = list(input())
        map_list.append(map_input)
        if '2' in map_input:
            source = [i, map_input.index('2')]

    visited = [[0] * 16 for _ in range(16)]
    answer = maze(map_list, source)

    print('#{} {}'.format(tc, answer))