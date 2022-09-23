# 2117 홈 방법 서비스
# 220923

'''
설계시간 11:00~11:30
구현시간 11:31~11:57
'''

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list()
    home = 0

    for _ in range(N):
        arrInput = list(map(int, input().split()))
        home += arrInput.count(1)
        arr.append(arrInput)

    # K의 최대값 구하기. k가 가능한 최대값 : K-1
    maxK = 1
    while True:
        if home*M > 2*(maxK**2) - 2*maxK +1:
            maxK += 1
        else:
            break
    
    answer = 0

    # 방범 서비스가 k값일때 첫 칸의 위치 (ki, kj) 구해서 적용
    for k in range(1, maxK):
        for ki in range((-(2*(k-1))), (N)):
            for kj in range((-k+1), (N+1-k)):
                home = 0
                # 방범 서비스구역 안에서 방범 서비스에 해당하는 칸 구하기
                for i in range(2*k-1):
                    for j in range(abs((k-1)-i),(2*k-1) - abs((k-1)-i)):
                        # 인덱스 안에 있는지 확인
                        if 0 <= ki + i < N and 0 <= kj + j < N:
                            if arr[ki+i][kj+j] == 1:
                                home += 1
                # 손해를 보지 않으면서
                if home * M >= 2*(k**2) - 2*k+1 :
                    # 정답보다 집의 개수가 더 크면 업데이트
                    if answer < home:
                        answer = home

    print('#{} {}'.format(tc, answer))