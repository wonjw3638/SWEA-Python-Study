T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tasks = []
    for _ in range(N):
        tasks.append(tuple(map(int, input().split())))
    
    tasks.sort(key=lambda x:(x[1], x[0]))
    answer = 1
    end = tasks[0][1]

    for idx, task in enumerate(tasks):
        if idx == 0 or task[0] < end: continue
        answer += 1
        end = task[1]

    print('#{} {}'.format(tc, answer))