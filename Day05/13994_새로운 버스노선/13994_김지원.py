# 13994 - 새로운 버스노선
# 220812

import sys
sys.stdin = open('input.txt','r')

T = int(input())

def my_max(a_list):
    answer = a_list[0]
    for a in a_list:
        if a > answer:
            answer = a
    return answer

for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 1001  # 1~1000 인데 index 헷갈리니까 1001개 생성

    for _ in range(N):
        bus_info = list(map(int, input().split()))

        bus, start, end = bus_info[0], bus_info[1], bus_info[2]
        if bus == 1: # 일반버스 일 때 
            for stop in range(start, end + 1):
                bus_stop[stop] += 1
        elif bus == 2: # 급행버스 일 때 
            num = start%2
            for stop in range(start, end):
                if (stop % 2) == num:   # 홀/짝 결과가 같을 때만 방문
                    bus_stop[stop] += 1
            bus_stop[end] += 1   # 도착지점 따로 추가
        else: # 광역 급행일 때
            if start%2: # 홀수 일 때
                for stop in range(start, end):
                    if ((stop%3) == 0 and (stop%10) != 0):
                        bus_stop[stop] += 1
                bus_stop[end] += 1
            else: # 짝수 일 때
                for stop in range(start, end):
                    if (stop%4) == 0:
                        bus_stop[stop] += 1
                bus_stop[end] += 1

    print('#{} {}'.format(tc, my_max(bus_stop)))