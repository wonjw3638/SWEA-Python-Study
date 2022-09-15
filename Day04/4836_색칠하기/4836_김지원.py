# 4836_색칠하기
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    color = [[0] * 10 for _ in range(10)]
    violet = 0  # 보라색 개수
    for _ in range(N):
        si, sj, ei, ej, c = list(map(int, input().split()))

        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                if color[i][j] == 0:
                    color[i][j] = c
                elif ((color[i][j] != 0) and (color[i][j] < 3)):  # 다른 색으로 칠해져있던 칸
                    violet += 1
                    color[i][j] += c   # 보라색 색칠 color[i][j] = 3
                else: # 이미 같은색으로 칠해진 칸
                    continue
        
    print('#{} {}'.format(tc, violet))