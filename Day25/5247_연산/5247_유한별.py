from collections import deque

def bfs():
    visited = set()
    q = deque()
    q.append((N, 0))
    
    while q:
        num, cnt = q.popleft()
        for next_num in (num+1, num-1, num*2, num-10):
            if 0 < next_num <= 1000000 and next_num not in visited:
                if next_num == M:
                    return cnt+1
                visited.add(next_num)
                q.append((next_num, cnt+1))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, bfs()))