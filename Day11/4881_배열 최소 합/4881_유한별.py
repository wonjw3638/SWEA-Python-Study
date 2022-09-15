# 4881_배열 최소 합
# 2022-08-23

def my_min(a, b):
    if a < b: return a
    else : return b


def dfs(j, my_sum):
    global min_sum

    if j == N:
        min_sum = my_min(min_sum, my_sum)
        return
    else:
        for i in range(N):
            if visited[i] != 1 and my_sum+table[i][j] < min_sum:
                visited[i] = 1
                dfs(j+1, my_sum+table[i][j])
                visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = list()
    visited = [0 for _ in range(N)]
    min_sum = 0b1111111111111111

    for _ in range(N):
        table.append(list(map(int, input().split())))
    
    dfs(0, 0)
    print('#{} {}'.format(tc, min_sum))