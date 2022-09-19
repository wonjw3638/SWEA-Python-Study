# 4843_특별한 정렬
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt','r')

def find_max_idx(arr) : # max값의 idx를 찾아 return
    max_V = arr[0]
    max_idx = 0
    for i, v in enumerate(arr) :
        if max_V < v :
            max_V = v
            max_idx = i
    return max_idx

def find_min_idx(arr) : # min값의 idx를 찾아 return
    min_V = arr[0]
    min_idx = 0
    for i, v in enumerate(arr) :
        if min_V > v :
            min_V = v
            min_idx = i
    return min_idx

def change_arr(arr, idx) : # 홀수번째(짝수idx)는 남은 값들 중 max값으로, 짝수번째(홀수idx)는 남은 값들 중 min값으로 교환해줌
    if idx % 2 == 0 :
        m_idx = find_max_idx(arr[idx:])
    else :
        m_idx = find_min_idx(arr[idx:])
    arr[idx], arr[idx + m_idx] = arr[idx + m_idx], arr[idx] # 함수를 정렬되지 않은 뒤쪽만 시행하기 때문에 구한 m_idx를 현재 idx에서 더해줘야함

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    nums = list(map(int, input().split()))

    print('#{} '.format(test_case), end='')
    for idx in range(10) : # 출력은 10개이므로 10번만 반복
        change_arr(nums, idx)
        print(nums[idx], end=' ')
    print()