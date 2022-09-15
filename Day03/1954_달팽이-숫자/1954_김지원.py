# 1954_달팽이 숫자
# 220810

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 우하좌상 순으로 
di = [0, +1, 0, -1]
dj = [+1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    num_list = [[0] * N for _ in range(N)]
    value = 1
    ni = nj = 0
    for n in range(N, 0, -2):  # 겉에서부터 상자 하나씩 안으로 들어감. 한바퀴 도는거 반복문.
        for d in range(4):    #우하좌상으로 움직임
            while (0 <= ni < N) and (0 <= nj < N): # 범위 벗어나면 x
                num_list[ni][nj] = value   # 범위 안에 있으면 값 업데이트 
                if not ((0 <= ni+di[d] < N) and (0 <= nj+dj[d] < N)): # 그 다음 이동 위치가 범위 벗어나면 탈출, 이동방향 바꿈
                    break
                if num_list[ni + di[d]][nj + dj[d]] != 0: # 다음 이동할 곳에 이미 값이 있는 경우 탈출, 방향 바꿈
                    break
                value += 1
                ni += di[d]
                nj += dj[d]

    print('#{}'.format(tc))
    for li in num_list:
        print(*li)