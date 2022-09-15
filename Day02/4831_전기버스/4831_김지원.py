# 4831_전기버스
# 220809

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))
    cnt, loc, i = 0, 0, K

    while loc + i < N:   # 도착한 경우 반복문 탈출
        if i == 0:
            cnt = 0
            break
        if (loc + i) in charge:  # 이동하는 정류장에 에 충전소가 있으면 이동
            loc += i   # 해당 위치로 이동 
            cnt += 1   # 충전횟수 +1
            i = K
        else:
            i -= 1 # 충전소가 없는 경우 한칸 앞에 충전소 있나 확인

    print('#{} {}'.format(tc, cnt))