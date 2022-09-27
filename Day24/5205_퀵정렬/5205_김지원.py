# 5202 퀵 정렬
# 220927

import sys
sys.stdin = open('input.txt', 'r')

def quickSort(arr, l, r):
    if l < r:
        # 피봇값 배치
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

def partition(arr, l, r):
    # 피봇값 설정
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i<= j and arr[j] >= p:
            j -= 1
        
        # i는 p보다 큰 값을 만나고, j는 p보다 작은 값을 만났는 데, i < j 이면 둘이 자리 바꾸기
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 피봇값 위치 변경
    arr[l], arr[j] = arr[j], arr[l]
    return j 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, N-1)

    print('#{} {}'.format(tc, arr[N//2]))