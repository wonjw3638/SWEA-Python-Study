import sys
sys.stdin = open('input.txt','r')
bun = int(input())
for he in range(1,bun+1) :
    n, m = map(int, input().split())
    pan = []
    for i in range(n):
        pan.append(input())

    # 가로인 경우
    row = []
    for i in range(n):
        # 행렬의 범위에서 주어진 길이만큼의 단어를 찾아야 하므로 n-m만큼의 범위에서 찾아야 하는데  range는 -1 까지 찾으므로 +1 해주기
        for j in range(n-m+1):
            if  pan[i][j:j+n] == pan[i][j:j+n][::-1]:
                row.append(pan[i][j:j+n])
                print('#{}'.format(he), end=' ')
                print(''.join(row))
    # 세로인 경우
    for i in range(n):
        for j in range(n-m+1):
            col = []
            for k in range(m) :
                # 열을 세로로 쌓아주기
                col += pan[j+k][i]
            if col == col[::-1]:
                print('#{}'.format(he), end=' ')
                print(''.join(col))


