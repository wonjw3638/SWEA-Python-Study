# 5209 최소 생산 비용
# 220928

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs():
    visited = set()
    visited.add(N)

    while queue:
        n, cnt = queue.popleft()
        cnt += 1

        # 연산 진행
        for m in (n+1, n-1, 2*n, n-10):
            # 연산 결과가 범위 내에 있으면서 방문한 적 없는 값
            if (0 < m <= 1000000) and (m not in visited):
                # 찾는 값과 같은 경우 바로 반환
                if m == M:
                    return cnt
                visited.add(m)
                queue.append((m, cnt))

    return


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    queue = deque()
    queue.append((N, 0))
    # 현재 숫자, 카운트
    answer = bfs()

    print('#{} {}'.format(tc, answer))