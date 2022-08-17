# 2005_파스칼의 삼각형
# 2022-08-17

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    pascal = [[0 for _ in range(N)] for _ in range(N)]
    pascal[0][0] = 1
    print('#{}'.format(tc))
    print(pascal[0][0])
    for i in range(1, N) :
        for j in range(i + 1) :
            if j == 0 or j == i :
                pascal[i][j] = 1
            else :
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            print(pascal[i][j], end=' ')
        print()