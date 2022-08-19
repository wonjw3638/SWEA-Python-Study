import sys
sys.stdin = open('input.txt','r')
bun = int(input())
for he in range(1, bun+1) :
    n = int(input())
    
    # 초기값 설정
    arr = [[0] * (n+1) for _ in range(n+1)]
    arr[1][1] = 1
    
    # 값을 계속 더해주기
    for i in range(2, n+1) :
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    
    print('#{}'.format(he))
    for i in range(1, n+1) :
        for j in range(1, i+1):
            print(arr[i][j], end = ' ')
        print()