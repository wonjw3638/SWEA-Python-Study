# 2382 미생물 격리
# 220923

'''
설계시간 13:30~13:40
구현시간 13:54~14:20 14:45~15:20
'''

# import sys
# sys.stdin = open('input.txt', 'r')

# d값에 따른 델타 이동
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

dReverse = {
    1 : 2,
    2 : 1,
    3 : 4,
    4 : 3,
}

T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    arr = [[0]*N for _ in range(N)]
    for _ in range(K):
        # 입력 값 배열에 미생물 수, 이동방향, 이동 여부 표시할 값 넣기
        i, j, c, d = list(map(int, input().split()))
        arr[i][j] = [[c, d]]

    # 주어진 시간만큼 반복
    for _ in range(M):
        # 이동한 후의 배열
        arrMove = [[0]*N for _ in range(N)]
        # 여러 군집이 만나는 경우
        check = list()
        for i in range(N):
            for j in range(N):
                # 미생물이 있는 칸만 보기
                if arr[i][j]:
                    c, d = arr[i][j][0]
                    ni = i + di[d]
                    nj = j + dj[d]
                    
                    # 이동한 결과가 용액에 닿는 경우
                    if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                        c = c//2
                        d = dReverse.get(d)
                        arrMove[ni][nj] = [[c, d]]
                    else:
                        # 이동한 곳에 미생물 군집이 이미 존재하는 경우
                        if arrMove[ni][nj]:
                            if not [ni, nj] in check:
                                check.append([ni, nj])
                            arrMove[ni][nj].append([c, d])
                        # 이동한 곳이 비어있는 경우
                        else:
                            arrMove[ni][nj] = [[c, d]]
        
        # 중복된 군집 정리.
        for i, j in check:
            tmpC = arrMove[i][j][0][0]
            direction = arrMove[i][j][0][1]
            totalC = tmpC

            for c, d in arrMove[i][j][1:]:
                totalC += c
                if c > tmpC:
                    tmpC = c
                    direction = d
                else:
                    continue
        
            arrMove[i][j] = [[totalC, direction]]
        
        # 이동한 결과를 이동전 배열로 딥카피
        arr = [arrMove[i][:] for i in range(N)]
    
    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                answer += arr[i][j][0][0]


    print('#{} {}'.format(tc, answer))