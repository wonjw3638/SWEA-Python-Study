# 4875_미로
# 220823
'''
설계 15:25~15:29
구현 15:33~16:28
'''

import sys
sys.stdin = open('input.txt','rt')

def maze(src):
    # 위, 오른쪽, 아래, 왼쪽 탐색하는 델타 생성
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    top = -1
    pos = src
    visited[pos[0]][pos[1]] = 1
    cnt = 0
    while True:
        cnt += 1
        for k in range(4):
            if not ((0 <= pos[0] + di[k] < N) and (0 <= pos[1] + dj[k] < N)):
                continue
            # 도착지점인 경우 - break
            if arr[pos[0] + di[k]][pos[1] + dj[k]] == 3:
                return 1
            elif arr[pos[0] + di[k]][pos[1] + dj[k]] == 0:
                # 이미 방문한 노드
                if visited[pos[0] + di[k]][pos[1] + dj[k]] == 1:
                    continue
                # 방문한 적 없는 노드
                else:
                    top += 1
                    stack[top] = pos
                    pos = [(pos[0] + di[k]), (pos[1] + dj[k])]
                    visited[pos[0]][pos[1]] = 1
                    break
        # 더 이상 갈 수 없는 곳이 없는 경우
        else:
            # 스택이 비어있음
            if top == -1:
                return 0
            # 스택에 값이 있음
            else:
                pos = stack[top]
                top -= 1

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    visited = [[0]* N for _ in range(N)]
    stack = [''] * (N**2)
    arr = list()

    # 입력된 문자열로 2차원 리스트 만들기
    for n in range(N):
        string = input()
        tmp = list()
        for i, s in enumerate(string):
            tmp.append(int(s))
            # 출발지점의 좌표 찾기
            if s == '2':
                src = [n, i]
        arr.append(tmp)

    answer = maze(src)
    
    print('#{} {}'.format(tc, answer))