# 1225_암호생성기
# 2022-08-24

# min 함수 대체
def my_min(my_arr):
    minV = 2147483647
    for a in my_arr:
        if minV > a:
            minV = a
    return minV


# 주어진 범위가 int의 범위이므로 최악의 경우
# 21억 * 8 = 약 170억회의 연산을 해야될 수 있음
# 따라서 연산 수를 최대한 줄여주기 위한 전처리 필요
# 8사이클이 돌면 모든 숫자가 120씩 감소하고 원래의 자리로 돌아옴
# 따라서 120의 배수를 빼주고 나머지 값들로만 연산하면 됨
def preprocessing(minV):
    del_cycle = minV // 120
    for a in arr:
        a -= del_cycle * 120


# 문제에서 주어진 1사이클 돌기
# 만약 중간에 원하는 값이 나올 경우 True 리턴
def cycle():
    global arr
    for i in range(1, 6):
        if arr[0] > i:
            arr.append(arr[0]-i)
            del arr[0]
        else:
            arr.append(0)
            del arr[0]
            return True
    return False


for tc in range(1, 11):
    _ = int(input())
    arr = list(map(int, input().split()))

    arr_min = my_min(arr)
    preprocessing(arr_min)

    while True:
        is_end = cycle()
        if is_end:
            break
    
    print('#{}'.format(tc), *arr)