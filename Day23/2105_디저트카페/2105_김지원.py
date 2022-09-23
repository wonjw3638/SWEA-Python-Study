# 2105 디저트 카페
# 220923

'''
설계시간 09:13 ~ 09:16
구현시간 09:17 ~ 10:51
'''
import sys
sys.stdin = open('input.txt', 'r')

# 이동방향 -> 오른쪽 대각선 위, 오른쪽 대각선 아래, 왼쪽 대각선 아래, 왼쪽 대각선 위
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(i, j, cnt, d, visited):
    global answer

    # 출발점으로 돌아온 경우에만 최종값 비교
    if i == si and j == sj:
        if cnt > answer:
            answer = cnt
            return


    # 같은 방향으로 한번 더 가거나, 다음 방향으로 바꾸거나.
    # 아직 한 바퀴 다 안돈 경우
    if len(d) < 4 :
        direction = [d[-1], d[-1]+1]
    # 한 바퀴를 다 돈 경우
    else:
        direction = [d[-1]]

    for dn in direction:
        ni = i + di[dn]
        nj = j + dj[dn]

        # 배열 인덱스 범위 안에 있는 경우
        if 0 <= ni < N and 0 <= nj < N:
            # 안먹어본 디저트인 경우
            if not (arr[ni][nj] in visited):
                # 원본 훼손 방지
                visit = visited[:]
                visit.append(arr[ni][nj])
                if dn == d[-1]:
                    dfs(ni, nj, cnt+1, d, visit)
                else:
                    # 원본 훼손 방지
                    dd = d[:]
                    dd.append(dn)
                    dfs(ni, nj, cnt+1, dd, visit)

    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for si in range(N):
        for sj in range(N):
            visited = list()
            dfs(si, sj, 0, [0], visited)

    # 디저트를 먹을 수 없는 경우엔 -1
    if answer == 0:
        answer = -1

    print('#{} {}'.format(tc, answer))