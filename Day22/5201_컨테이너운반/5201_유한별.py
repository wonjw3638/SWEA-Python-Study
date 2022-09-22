import heapq

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    trucks = list(map(int, input().split()))
    heap = []

    for truck in trucks:
        heapq.heappush(heap, (-truck, truck))

    answer = 0
    for weight in weights:
        if not heap:
            break
        if heap[0][1] < weight:
            continue
        tmp = heapq.heappop(heap)
        answer += weight
        heapq.heappush(heap, (-(tmp[1]-weight), tmp[1]-weight))

    print('#{} {}'.format(tc, answer))