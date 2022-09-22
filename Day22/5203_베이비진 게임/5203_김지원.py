# 5203 베이비진 게임
# 220922

'''
15:59~16:15
'''

import sys
sys.stdin = open('input.txt', 'r')

# arr에서 n개 고르는 조합 함수
def comb(arr, n):
    result = list()

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for j in comb(arr[i+1:], n-1):
            result.append([elem] + j)

    return result

# babyjin 판별 함수
def babyjin(arr):
    comb_arr = comb(arr, 3)
    for i in range(len(comb_arr)):
        ans = babyjinCheck(comb_arr[i])
        if ans == True:
            return 1
    return 0

# babyjin 확인하는 함수
def babyjinCheck(arr):
    arr.sort()
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return True
    else:
        if arr[0] == arr[1]-1:
            if arr[1] == arr[2]-1:
                return True
        return False

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr1 = list()
    arr2 = list()

    for i in range(len(arr)):
        if i % 2:
            arr2.append(arr[i])
        else:
            arr1.append(arr[i])

    answer = 0
    for idx in range(5):
        if babyjin(arr1[:idx+3]) == True:
            answer = 1
            break
        else:
            if babyjin(arr2[:idx+3]) == True:
                answer = 2
                break
            else:
                continue

    print('#{} {}'.format(tc, answer))