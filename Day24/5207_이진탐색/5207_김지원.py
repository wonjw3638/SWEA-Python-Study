# 5207 이진탐색
# 220927

'''
설계시간 5 
구현시간 14:00~14:25
'''

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    answer = 0

    for b in B:
        l, r = 0, N-1
        m = (l+r)//2

        if A[m] == b:
            answer += 1
            continue
        elif A[m] > b:
            r = m - 1
            # check = False 왼쪽 선택
            check = False
        else:
            l = m + 1
            # check = True 오른쪽 선택
            check = True

        while l <= r:
            if l == r:
                if A[l] == b:
                    answer += 1
                    break
                else:
                    break

            m = (l+r) // 2
            if A[m] == b:
                answer += 1
                break
            elif A[m] > b:
                # 또 같은 왼쪽 구간 선택
                if check == False:
                    break
                # 오른쪽 구간 선택
                else:
                    check = False
                    r = m - 1
            else:
                if check == True:
                    break
                else:
                    l = m + 1
                    check = True
            

    print('#{} {}'.format(tc, answer))