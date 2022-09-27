def bin_search(item):
    left = 0
    right = N-1
    middle = (left+right)//2
    tmp = ''
    flag, check = False, False
    while left <= right:
        if item == dest[middle]:
            tmp += 'm'
            flag = True
            break
        elif item < dest[middle]:
            tmp += 'l'
            right = middle-1
        else:
            tmp += 'r'
            left = middle+1
        middle = (left+right)//2

    check = True
    can_cnt = ['rr', 'll',]
#    if len(tmp) == 1:
    for i in range(len(tmp)-1):
        if tmp[i:i+2] in can_cnt:
            check = False
    if flag and check:
        return True
    return False


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    dest = list(map(int, input().split()))
    src = list(map(int, input().split()))
    dest.sort()

    answer = 0
    for item in src:
        if bin_search(item): answer += 1
    print('#{} {}'.format(tc, answer))