def dfs(depth):
    global answer
    if depth == exchange:
        answer = max(answer, int(''.join(map(str, arr))))
        return
    for i in range(n):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            if visited.get((int(''.join(map(str, arr))), depth), 1):
                dfs(depth+1)
                visited[(int(''.join(map(str, arr))), depth)] = 0
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T+1):
    arr, exchange = input().split()
    exchange = int(exchange)
    arr = list(map(int, list(arr)))
    n = len(arr)
    answer = float('-INF')
    visited = {}

    dfs(0)
    print('#{} {}'.format(tc, answer))