# 1486_장훈이의 높은 선반
# 220916

'''
09:30~09:42
'''
import sys
sys.stdin = open('input.txt','rt')

T = int(input())

def combi(Arr, N):
    result = list()

    if N == 0:
        return [[]]
    else:
        for i in range(len(Arr)):
            elem = [Arr[i]]
            for j in combi(Arr[i+1:], N-1):
                result.append(elem + j)
    return result

for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    H_list = list(map(int, input().split()))
    answer = 987654312
    n = 0
    while n < N:
        n += 1
        h_sum_list = combi(H_list, n)

        for idx in range(len(h_sum_list)):
            h_sum_list[idx] = sum(h_sum_list[idx])

        tmp = list()
        for h_sum in h_sum_list:
            # 키의 합이 더 큰경우에 차이값 저장
            if h_sum >= B:
                tmp.append(h_sum - B)
        # 더 큰 키의 합 경우의 수가 나온 경우
        if tmp:
            min_tmp = min(tmp)
            answer = min(min_tmp, answer)
            if answer == 0:
                break

    print('#{} {}'.format(tc, answer))