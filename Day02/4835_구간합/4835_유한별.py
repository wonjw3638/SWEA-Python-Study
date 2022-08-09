T = int(input())

for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    s_idx = 0 # 시작 인덱스
    e_idx = M - 1 # 끝 인덱스
    sum_nums = 0

    # 숫자들의 시작 인덱스 ~ 끝 인덱스까지의 값을 합함    
    for idx in range(s_idx, e_idx + 1) :
        sum_nums += nums[idx]
    
    max_nums = sum_nums
    min_nums = sum_nums

    while e_idx < N - 1 :
        # 오른쪽 한 칸 이동(왼쪽 끝 값 삭제 + 오른쪽 한 칸 뒤 추가)
        sum_nums -= nums[s_idx]
        s_idx += 1
        e_idx += 1
        sum_nums += nums[e_idx]
        if max_nums < sum_nums :
            max_nums = sum_nums
        if min_nums > sum_nums :
            min_nums = sum_nums
        
    print('#{} {}'.format(test_case, max_nums - min_nums))