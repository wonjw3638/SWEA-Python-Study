# 5099_피자 굽기
# 2022-08-25

def cycle():
    global oven
    global pizza
    global leftover
    global pizza_idx

    check = 0
    last_idx = 0

    # 오븐을 한바퀴 돌림
    while check < N:
        # 만약에 오븐이 비어있고, 남아있는 피자가 있다면
        if oven[check][0] == 0 and pizza_idx < M:
            pizza_idx += 1
            oven[check] = [pizza.pop(0), pizza_idx]
        # 오븐의 해당 위치가 차있을 때 -> index 기록
        if oven[check][0]:
            last_idx = oven[check][1]
        # 치즈 절반 녹이기
        oven[check][0] //= 2
        check += 1

    return last_idx


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = [[0, 0] for _ in range(N)]

    for i in range(N):
        oven[i] = [pizza.pop(0), i+1]
    pizza_idx = N
    
    while True :
        tmp = cycle()
        if tmp: result = tmp
        # 오븐이 비어있을 경우
        else: break
    
    print('#{} {}'.format(tc, result))