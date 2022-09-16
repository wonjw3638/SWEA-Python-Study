T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = -1
    num = 1
    while True:
        if num ** 3 < N: num += 1
        else:
            if num ** 3 == N: answer = num 
            break
    print('#{} {}'.format(tc, answer))