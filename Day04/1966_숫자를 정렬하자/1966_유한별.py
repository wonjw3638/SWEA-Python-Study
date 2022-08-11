# 1966_숫자를 정렬하자
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt')

def my_merge(arr, s_idx, m_idx, e_idx) :
    i = s_idx
    j = m_idx + 1
    tmp_arr = []
    while i <= m_idx and j <= e_idx : # 양쪽 가장 앞부분부터 비교 -> 더 작은 값을 tmp_arr에 넣어줌
        if arr[i] <= arr[j] :
            tmp_arr.append(arr[i])
            i += 1
        else :
            tmp_arr.append(arr[j])
            j += 1
    while i <= m_idx : # 둘 중 남은게 있을 경우 나머지 넣어주기
        tmp_arr.append(arr[i])
        i += 1
    while j <= e_idx : # 둘 중 남은게 있을 경우 나머지 넣어주기
        tmp_arr.append(arr[j])
        j += 1
    arr[s_idx:e_idx+1] = tmp_arr[:] # 새롭게 만들어진 arr 기존 arr에 반영

def my_sort(arr, s_idx, e_idx) :
    if s_idx < e_idx :
        m_idx = (s_idx + e_idx)//2
        my_sort(arr, s_idx, m_idx) # 좌측 절반 정렬
        my_sort(arr, m_idx+1, e_idx) # 우측 절반 정렬
        my_merge(arr, s_idx, m_idx, e_idx) # 병합


# merge sort 연습
T = int(input())

for test_case in range(1, T+1) : 
    N = int(input())
    arr = list(map(int, input().split()))
    my_sort(arr, 0, N-1)
    print('#{}'.format(test_case), end=' ')
    for i in arr :
        print(i, end=' ')
    print()