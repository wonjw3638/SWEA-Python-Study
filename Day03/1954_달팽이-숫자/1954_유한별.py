# 1954_달팽이 숫자
# 2022-08-10

# 작은 달팽이 한 마리가 내게로 다가와
# 작은 목소리로 속삭여줬어

# import sys
# sys.stdin = open('input.txt','r')

def snail(i, j, cnt, d) :
    global N
    global shell
    shell[i][j] = cnt # 제대로 들어왔으니 위치에 맞는 값 넣어주기

    if cnt == N ** 2 : # 다채웠으면 리턴
        return

    if d == 'R' :
        if shell[i][j+1]!= 0 : # 오른쪽 벽 만나면 아래로 방향 전환
            snail(i, j, cnt, 'D')
        else : # 아니면 전진!
            snail(i, j+1, cnt+1, d)
    elif d == 'D' :
        if shell[i+1][j]!= 0 : # 아래쪽 벽 만나면 왼쪽으로 방향 전환
            snail(i, j, cnt, 'L')
        else : # 아니면 전진!!
            snail(i+1, j, cnt+1, d)
    elif d == 'L' : # 왼쪽 벽 만나면 로 방향 전환
        if shell[i][j-1]!= 0 :
            snail(i, j, cnt, 'U')
        else : # 아니면 전진!!!
            snail(i, j-1, cnt+1, d)
    else : # 위쪽 벽 만나면 오른쪽으로 방향 전환
        if shell[i-1][j]!= 0 :
            snail(i, j, cnt, 'R')
        else : # 아니면 전진!!!
            snail(i-1, j, cnt+1, d)


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    shell = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(N + 2) : # 껍데기 외부에 -1로 벽을 쳐줌
        shell[0][i] = -1
        shell[N + 1][i] = -1
        shell[i][0] = -1
        shell[i][N+1] = -1

    snail(1, 1, 1, 'R')
    print('#{}'.format(test_case))
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            print(shell[i][j], end =' ')
        print()

# 언젠가 먼 훗날에 저 넓고 거칠은
# 세상 끝 바다로 갈거라고