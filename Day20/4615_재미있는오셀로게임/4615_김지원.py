# 4615 재미있는 오셀로 게임
# 220920

import sys
sys.stdin = open('input.txt', 'r')

color = {
    1 : 2,
    2 : 1,
}
di = [-1, 0, 1, 0, -1, -1, 1, 1]
dj = [0, 1, 0, -1, -1, 1, 1, -1]
 
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
 
    map_list = [ [0] * (N + 1) for _ in range(N + 1) ]
    map_list[N//2][N//2] = map_list[N//2 + 1][N//2 + 1] = 2
    map_list[N//2 + 1][N//2] = map_list[N//2][N//2 + 1] = 1
 
 
    for _ in range(M):
        i, j, c = list(map(int, input().split()))
 
        map_list[i][j] = c
 
        for d in range(8):
            stack = [[0, 0]] * (N**2)
            top = -1
            for k in range(1,N):
                if (1 <= i + di[d] * k < N+1) and (1 <= j + dj[d] * k < N+1) :
                    if map_list[i + di[d] * k][j + dj[d] * k] == color.get(c):
                        top += 1
                        stack[top] = [i + di[d] * k, j + dj[d] * k]
                    elif map_list[i + di[d] * k][j + dj[d] * k] == c:
                        while top >= 0:
                            map_list[stack[top][0]][stack[top][1]] = c
                            top -= 1
                        break
                    else:
                        break
                else:
                    break
         
    w = b = 0
 
    for i in range(1, N+1):
        for j in range(1, N+1):
            if map_list[i][j] == 1:
                b += 1
            elif map_list[i][j] == 2:
                w += 1
     
    print('#{} {} {}'.format(tc, b, w))