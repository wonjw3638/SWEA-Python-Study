# 2819 격자판의_숫자_이어_붙이기
# 220922

'''
'''

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# DFS
def dfs(i, j):
    stack = list()
    
    # 위치값, 그동안 모아온 문자열 값
    stack.append([i, j, arr[i][j]])

    while stack:
        i, j, string = stack.pop()
        # 모아온 문자열의 길이가 7이면 끝!
        if len(string) == 7:
            tmp.append(string)
            continue
        
        # 원본 훼손 방지
        origin_string = string

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < 4 and 0 <= nj < 4 :
                # 방문한 곳 또 방문해도 되니까 그냥 이동
                string = origin_string + arr[ni][nj]
                stack.append([ni, nj, string])

T = int(input())

for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    tmp = list()

    # 모든 배열의 원소값에 대해 dfs돌리기
    for i in range(4):
        for j in range(4):
            dfs(i, j)

    # 중복제거 후에 갯수 세기
    answer = len(set(tmp))

    print('#{} {}'.format(tc, answer))