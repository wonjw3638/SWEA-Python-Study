# 1225 암호생성기
# 220824
'''
설계 3m
구현 15m
'''
import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    front = 0
    rear = 7

    tc = int(input())
    queue = list(map(int, input().split()))
    chk = False

    while True:
        # 반복문 탈출 확인 변수
        if chk == True: 
            break
        # 사이클 돌기 1~5까지 빼기
        for k in range(1,6):
            tmp = queue[front] - k
            # 만약 뺀 값이 0보다 작거나 같으면 반복문 탈출
            if tmp <= 0:
                tmp = 0
                chk = True
            # front에 위치한 값 제거, 앞으로 한칸씩 당김
            for idx in range(1, rear + 1):
                queue[idx-1] = queue[idx]
            # rear에 계산한 값 삽입
            queue[rear] = tmp
            if chk == True:
                break
            else:
                continue
    
    # 문자열로 변환, 출력형식 맞춰줌
    answer = ''
    for q in queue:
        answer += (str(q) + ' ')

    print('#{} {}'.format(tc, answer))