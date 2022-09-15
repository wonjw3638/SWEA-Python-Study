# 기본 베이스는 그리디 알고리즘 참조
# 각 충전소에서 가장 먼 거리의 충전소까지 이동
# 만약 충전을 가득해도 다음 충전소까지 도착 못하면 0 반환함

T = int(input())

for test_case in range(1, T+1) :
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    idx, cnt = 0, 0

    print('#{}'.format(test_case), end=' ')
    # 도착할 때까지 while문으로 반복 재생
    while idx < N :
        # 충전 후 갈 수 있는 거리 (K ~ 1)내에 충전소 있는지 확인 
        for dest in range(K, 0, -1) :
            # 만약 종착지에 도착할 수 있으면 지금까지 충전 횟수 출력 후 종료
            if idx + dest == N :
                idx += dest
                print(cnt)
                break
            # 이동거리 내에 충전소가 있을 경우 가장 먼 거리의 충전소로 이동
            elif idx + dest in stations :
                cnt += 1
                idx += dest
                break
            else :
                continue
        # 갈 수 있는 곳이 없으면 0 출력 후 종료
        else :
            print(0)
            break