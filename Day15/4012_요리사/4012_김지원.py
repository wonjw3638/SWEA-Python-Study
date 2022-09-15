# 4012_요리사
# 220915
'''
14:
'''

import sys
sys.stdin = open('input.txt','rt')

T= int(input())

def combi(Arr, N):
    result = []

    if N == 0:
        return [[]]
    else:
        for i in range(len(Arr)):
            elem = [Arr[i]]
            for j in combi(Arr[i+1:], N-1):
                result.append(elem + j)
    
    return result

for tc in range(1, T+1):
    N = int(input())
    total = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    ingr = [i for i in range(N)]
    # 식재료 N//2 개를 사용해 음식 만들기 N C (N//2)
    ingr_combi = combi(ingr,N//2)
    print(ingr_combi)
    flavor = 987654312

    for idx in range(len(ingr_combi)):
        # 남은 식재료 조합
        ingr_other = list(set(ingr) - set(ingr_combi[idx]))
        food1 = food2 = 0

        # 선택한 재료들 중 2개씩 값 더하기
        ingC2_1 = combi(ingr_combi[idx], 2)
        for index in range(len(ingC2_1)):
            i, j = ingC2_1[index]
            food1 += arr[i][j] + arr[j][i]
        
        # 선택하지 않은 재료들 중 2개씩 값 더하기
        ingC2_2 = combi(ingr_other, 2)
        for index in range(len(ingC2_2)):
            i, j = ingC2_2[index]
            food2 += arr[i][j] + arr[j][i]

        tmp = abs(food1 - food2)

        if flavor > tmp:
            flavor = tmp

    print('#{} {}'.format(tc, flavor))