# 퀵소트 구현
def quick_sort(my_arr, n):
    # 길이가 1 이하일 때 정렬 필요 X
    if n <= 1:
        return my_arr
    # 0번째 값을 pivto으로 설정
    pivot = my_arr[0]
    left_arr, middle_arr, right_arr = [], [], []
    left_len, right_len = 0, 0
    for item in my_arr:
        # pivot보다 작을 경우 왼쪽 arr
        if item < pivot:
            left_len += 1
            left_arr.append(item)
        elif item == pivot:
            middle_arr.append(item)
        # pivot보다 클 경우 오른쪽 arr
        else:
            right_len += 1
            right_arr.append(item)
    # 재귀호출을 통해 모든 arr에 대해 함수 적용
    return quick_sort(left_arr, left_len) + middle_arr + quick_sort(right_arr, right_len)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(tc, quick_sort(arr, N)[N//2]))