T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_v = sum(heights)

    for i in range(1<<N):
        tmp = 0
        for j in range(N):
            if i & (1<<j):
                tmp += heights[j]
        if tmp >= B:
            min_v = min(tmp-B, min_v)
    
    print('#{} {}'.format(tc, min_v))