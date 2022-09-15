# 13994_새로운 버스 노선
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

def my_max(arr) : # 배열 안의 max값 찾기
    maxV = arr[0]
    for a in arr :
        if maxV < a :
            maxV = a
    return maxV

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    stations = [0 for _ in range(1001)]

    for _ in range(N) :
        bus_type, start, end = map(int, input().split()) # 입력 받아서 바로 처리

        if bus_type == 1 : # 버스가 일반버스(1)일 경우
            for i in range(start, end+1) : # 다 채우기
                stations[i] += 1

        elif bus_type == 2 : # 버스가 급행버스(2)일 경우
            for i in range(start, end+1, 2) : # +2 씩 넘어가면서 채우기
                stations[i] += 1

        else : # 버스가 광역 급행버스(3) 일 경우
            if start % 2 : # 시작 정류장이 홀수일 경우
                start = start + (0, 2, 1)[start % 3] # 시작 정류장을 3의 배수로 올림(?)해 줌
                for i in range(start, end+1, 3) : # +3씩 넘어가면서 채우기
                    if i % 10 == 0 : # 10의 배수 제외
                        continue
                    stations[i] += 1
            else : # 시작 정류장이 짝수일 경우
                start = start + (0, 3, 2, 1)[start % 4] # 시작 정류장을 4의 배수로 올림(?)해 줌
                for i in range(start, end+1, 4) : # +4씩 넘어가면서 채우기
                    stations[i] += 1
    
    print('#{} {}'.format(test_case, my_max(stations))) # 다 채우고 max 값 찾아 출력