import sys
sys.stdin = open('input.txt', 'r')

for he in range(1, 11) :
    D = int(input())
    height = list(map(int, input().split()))
    cnt = [0]*101
    for i in height:
        cnt[i] += 1


    bottom = 100
    top = 0
    for j in height:
        if j < bottom :
            bottom = i
        if j > top:
            top = i
    n = 0
    while n < D :
        cnt[top] -= 1
        cnt[top-1] += 1
        cnt[bottom] -= 1
        cnt[bottom+1] += 1
        while cnt[top] == 0:
            top -= 1
        while cnt[bottom] == 0:
            bottom += 1

        n += 1  # while문 빠져나가기 위해서 1씩 더해줌
    result = top - bottom

    print(f'#{he} {result}')