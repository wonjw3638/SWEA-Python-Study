# 1210_ladder1
# 220811

import sys
sys.stdin = open('input.txt','r')

for _ in range(10):
    T = int(input())
    ladders = []

    for _ in range(100):
        ladder = list(map(int, input().split()))
        ladders.append([0] + ladder + [0]) # index error 방지, 100 x 102
    
    j = -1
    for dest in range(102):   # 마지막줄 도착점 찾기
        if ladders[99][dest] == 2:
            j = dest
            break
        else: continue
    
    i = 99

    while i > 0:  # 가장 윗줄로 올라올 때까지 반복
        if ladders[i][j+1]:
            while ladders[i][j+1]:  # 오른쪽에 길이 있다면 0을 만날 때까지 오른쪽으로 이동
                j += 1
            i -= 1  # 0 만나면 위로 이동
        elif ladders[i][j-1]:  # 왼쪽에 길이 있다면
            while ladders[i][j-1]:  # 왼에 길이 있다면 0을 만날 때까지 오른쪽으로 이동
                j -= 1
            i -= 1  # 0 만나면 위로 이동
        else:  # 양쪽다 길 없으면
            i -= 1

    print('#{} {}'.format(T, j-1))  # index error 방지용으로 한줄 추가 한것 빼기