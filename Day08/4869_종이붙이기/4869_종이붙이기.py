# 4869_종이붙이기
# 2022-08-18

def fact(n) :
    return_value = 1
    while n >= 1 :
        return_value *= n
        n -= 1
    return return_value

T = int(input())

for tc in range(1, T+1) :
    N = int(input()) // 10
    # s는 20*20 정사각형의 개수
    # r은 10*20 직사각형의 개수
    # d_r은 r 2개로 이루어진 20*20 정사각형의 개수
    s = N // 2
    r, d_r = N - (s * 2), 0
    my_value = 0
    while s >= 0 :
        r += d_r * 2
        d_r = 0
        while r >= 0 :
            my_value += fact(s + r + d_r) // (fact(s) * fact(r) * fact(d_r))
            if r >= 2 :
                r -= 2
                d_r += 1
            else : break
        s -= 1
        r += 2
    print('#{} {}'.format(tc, my_value))