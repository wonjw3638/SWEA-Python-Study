import sys
sys.stdin = open('input.txt','r')
bun = int(input())
for he in range(1,bun+1) :
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0
    for i in range(n) :
        a1,b1, a2,b2, c= map(int, input().split())
        for j in range(a1, a2+1):
            for k in range(b1, b2+1):
                if c==1 :
                    arr[j][k] += 1
                else:
                    arr[j][k] += 2
    print(arr)

    for x in range(10) :
        for y in range(10) :
            if arr[x][y] ==3  :
                cnt += 1
    print('#{} {}'.format(he, cnt))
