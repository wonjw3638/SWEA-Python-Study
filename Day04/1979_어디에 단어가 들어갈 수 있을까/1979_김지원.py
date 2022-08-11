# 1979_어디에 단어가 들어갈 수 있을까
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())
di = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = list()
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    i = j = answer = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] :  # i, j 값이 1, count 시작
                for d in range(2):
                    if not (((0 <= i+di[d+2] < N) and (0 <= j+dj[d+2] < N)) and (puzzle[i+di[d+2]][j+dj[d+2]] == 1)): # 왼쪽에/ 위쪽에 값이 존재하지 않거나 0
                        cnt = 1        # 이웃한 칸 찾기
                        ni = i + di[d]
                        nj = j + dj[d]
                        while True:
                            if ((0 <= ni < N) and (0 <= nj < N)): # 오른쪽/아래쪽에 값이 존재
                                if puzzle[ni][nj]: # 그 값이 1
                                    cnt += 1
                                    ni += di[d]
                                    nj += dj[d]
                                else: break # 오른쪽/아래쪽 값이 0
                            else: break # 오른쪽/아래쪽 값이x
                        if cnt == K: 
                            answer += 1

    print('#{} {}'.format(tc, answer))
