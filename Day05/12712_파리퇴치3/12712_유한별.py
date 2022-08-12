# 12712_파리퇴치3
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

def find_max(arr) : # 두 값을 비교해 큰 값 return
    m = arr[0]
    for a in arr :
        if m < a :
            m = a
    return m
        
def spray(i, j, direction) :
    sum_fly = table[i][j]
    length = 1
    while length < M :
        for k in range(4) :
            next_i = i + (direction[k][0] * length)
            next_j = j + (direction[k][1] * length)
            if 0 <= next_i < N and  0 <= next_j < N :
                sum_fly += table[next_i][next_j]
        length += 1
    return sum_fly

T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    table = []
    for _ in range(N) :
        table.append(list(map(int, input().split())))
    
    direction_x = [(1,1), (1,-1), (-1,1), (-1,-1)]
    direction_p = [(1,0), (-1,0), (0,1), (0,-1)]
    max_fly = 0

    for i in range(N) :
        for j in range(N) :
            p = spray(i, j, direction_p)
            x = spray(i, j, direction_x)
            max_fly = find_max([max_fly, p, x])
    
    print('#{} {}'.format(test_case, max_fly))