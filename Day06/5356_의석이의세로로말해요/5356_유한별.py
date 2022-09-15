# 5356_의석이의세로로말해요
# 2022-08-16

# len 대체 함수
def my_len(arr) :
    cnt = 0
    for a in arr :
        cnt += 1
    return cnt


# max 대체 함수
def my_max(a, b) :
    if a >= b :
        return a
    else :
        return b


T = int(input())

for tc in range(1, T+1) :
    alphas = []
    n = 0
    for i in range(5) :
        alphas.append(list(input()))
        # 가장 길이가 긴 문자열의 길이 구하기
        n = my_max(my_len(alphas[i]), n)

    for i in range(5) :
        idx = 0
        m = my_len(alphas[i])
        while idx < n :
            # 만약 오른쪽 칸이 비어있으면 공백을 넣어줌
            if idx >= m - 1 :
                alphas[i].append('')
            idx += 1
    
    # 출력부 : 세로로 읽어주기
    print('#{}'.format(tc))
    for i in range(n) :
        for j in range(5) :
            print(alphas[j][i], end='')
    print()