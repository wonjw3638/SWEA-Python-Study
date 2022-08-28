# 1230_암호문3
# 220826

import sys
sys.stdin = open('input.txt','rt')

for tc in range(1, 11):
    # input값 받아오기
    N = int(input())
    pw = list(map(int, input().split()))
    M = int(input())
 
    command = list(input().split())
    idx = cmd = 0
 
    while cmd < M :
        # 명령어가 I인 경우
        if command[idx] == 'I':
            cmd += 1
            x = int(command[idx + 1])
            y = int(command[idx + 2])
 
            queue = [0] * y 
            rear = front = 0
 
            for i in range(y):
                queue[rear] = int(command[idx + 3 + i])
                rear += 1
             
            for j in range(y):
                pw.insert(x+j, queue[front])
                front += 1
             
            idx += (y + 3)
             
 
        # 명령어가 D인 경우
        elif command[idx] == 'D':
            cmd += 1
            x = int(command[idx + 1])
            y = int(command[idx + 2])
 
            for _ in range(y):
                del pw[x]
 
            idx += 3
 
        # 명령어가 A인 경우
        elif command[idx] == 'A':
            cmd += 1
            y = int(command[idx + 1])
 
            for i in range(1, y+1):
                pw.append(command[y + i])
             
            idx += (y + 2)
 
    answer = ''
 
    for i in range(10):
        answer += (str(pw[i]) + ' ')
 
    print('#{} {}'.format(tc, answer))