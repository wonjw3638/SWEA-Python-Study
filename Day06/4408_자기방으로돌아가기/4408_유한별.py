# 4408_자기 방으로 돌아가기
# 2022-08-16

#import sys
#sys.stdin = open('input.txt','r')

def my_max(arr) :
    maxV = 0
    for a in arr :
        if maxV < a :
            maxV = a
    return maxV

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    moves = []
    rooms = [0 for _ in range(201)]

    for i in range(N) :
        moves.append(list(map(int,input().split())))
        if moves[i][0] > moves[i][1] :
            moves[i][0], moves[i][1] = moves[i][1], moves[i][0]

        # 1~400을 1-200으로(홀짝 상관 안하게), 왼쪽이 오른쪽보다 작게 만들기
        if moves[i][0] % 2 :
            moves[i][0] = moves[i][0] + 1
        if moves[i][1] % 2 :
            moves[i][1] = moves[i][1] + 1
        moves[i][0] //= 2
        moves[i][1] //= 2

        # 한번 지나갈 때마다 복도 cnt + 1
        for j in range(moves[i][0], moves[i][1] + 1) :
            rooms[j] += 1

    # 가장 많이 지나간 복도의 수를 출력    
    print('#{} {}'.format(tc,(my_max(rooms))))