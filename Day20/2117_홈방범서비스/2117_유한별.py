def check(i, j):
    distance = []
    for home in homes:
        distance.append(abs(home[0]-i)+abs(home[1]-j)+1)
    distance.sort()
    n = len(distance)
    k = 1
    idx = 0
    max_idx = 0
    while idx < n:
        if distance[idx] <= k:
            idx += 1
        else:
            if idx*M >= (k**2+(k-1)**2):
                max_idx = idx
            k += 1
    if idx*M >= (k**2+(k-1)**2):
        max_idx = idx    
    return max_idx

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = []
    homes = []
    for i in range(N):
        table.append(list(map(int, input().split())))
        for j in range(N):
            if table[i][j] == 1:
                homes.append((i, j))

    answer = 0
    for i in range(N):
        for j in range(N):
            if i == 3 and j == 3:
                i = 3
            answer = max(answer, check(i, j))

    print('#{} {}'.format(tc, answer))