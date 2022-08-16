# 6485_삼성시의 버스 노선
# 220809

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    routes = []  # 버스가 지나가는 노선 정보
    for _ in range(N):
        routes.append(list(map(int, input().split()))) 
    
    P = int(input())

    answer = '#{}'.format(tc)
    for _ in range(P):
        C = int(input())
        bus = 0
        for route in routes:
            if ( route[0] <= C ) and ( route[1] >= C ):  # 선택한 정류장이 버스 노선 사이에 있으면 += 1
                bus += 1
        answer += (' ' + (str(bus)))
    
    print(answer)


# 방법 2 Runtime Error

# import sys
# sys.stdin = open('input.txt','r')

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     routes = []
#     max_station = 0
#     for _ in range(N):
#         route = list(map(int, input().split()))
#         routes.append(route)
#         if route[1] > max_station:
#             max_station = route[1]
    
#     stations = [0] * (max_station + 2)  # 합 더해나갈 거기때문에 마지막에 한칸 추가

#     for route in routes:
#         stations[route[0]] += 1  # 일일히 매번 더할 수 없어서 마지막에 더해가기 위해 범위 처음 값에 +1
#         stations[route[1] + 1] -= 1   # 범위 마지막+1 인 위치에 -1 추가
    
#     for i in range(1,max_station+2):   # index 1부터 끝까지 더해나가면 정류장의 총 개수 나옴
#         stations[i] += stations[i-1]
    
#     P = int(input())

#     answer = '#{}'.format(tc)
#     for _ in range(P):
#         C = int(input())
#         answer += (' ' + (str(stations[C])))
    
#     print(answer)



# 방법 3 Runtime Error

# import sys
# sys.stdin = open('input.txt','r')

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     stations = [0] * 5000
#     for _ in range(N):
#         route = list(map(int, input().split()))
#         for i in range(route[0], route[1] + 1):
#             stations[i] += 1
    
#     P = int(input())

#     answer = '#{}'.format(tc)
#     for _ in range(P):
#         C = int(input())
#         answer += (' ' + (str(stations[C])))
    
#     print(answer)