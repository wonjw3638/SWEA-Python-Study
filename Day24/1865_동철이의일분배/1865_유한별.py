def back_tracking(worker):
    global answer
    global p

    if worker == N:
        answer = max(answer, p)
        return
    
    for i in range(N):
        if visited[i]: continue
        if p*arr[worker][i] > answer:
            visited[i] = True
            p *= arr[worker][i]
            back_tracking(worker+1)
            visited[i] = False
            p /= arr[worker][i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [False for _ in range(N)]
    arr = []
    answer = 0
    for _ in range(N):
        arr.append(list(map(lambda x:x/100, list(map(int, input().split())))))
    
    p = 1
    back_tracking(0)
    answer *= 100

    print('#{} '.format(tc), end='')
    print('%.6f'%answer)