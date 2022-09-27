# 5204 병합정렬
# 220927

import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(arr):
    # 분할
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    # 병합
    def merge(low, mid, high):
        global cnt
        temp = list()
        l, h = low, mid

        # 왼쪽 리스트 마지막 값이 오른쪽 리스트 마지막 값보다 크면 cnt += 1
        if arr[mid-1] > arr[high-1]:
            cnt += 1 

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1

        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, N)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    
    # index 0부터 N-1까지
    merge_sort(arr)

    print('#{} {} {}'.format(tc, arr[(N//2)], cnt))