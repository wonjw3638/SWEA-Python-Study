def back_tracking(now):
    global cnt
    global answer

    if now >= N-1:
        answer = min(answer, cnt)
        return

    for move in range(1, stations[now]+1):
        if answer == cnt:
            return
        cnt += 1
        back_tracking(now+move)
        cnt -= 1


T = int(input())

for tc in range(1, T+1):
    answer = 0
    stations = list(map(int, input().split()))
    N = stations.pop(0)

    answer, cnt = float('INF'), 0
    back_tracking(0)
    print('#{} {}'.format(tc, answer-1))