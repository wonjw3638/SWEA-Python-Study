# 4836_색칠하기
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt','r')

T = int(input())

def put_color(r_idx, c_idx, color) :
    global table
    if table[r_idx][c_idx] == 0 : # 색이 칠해져 있지 않다면 해당 색으로
        table[r_idx][c_idx] = color
    elif table[r_idx][c_idx] != color : # 다른 색이 칠해져있다면 보라색으로
        table[r_idx][c_idx] += color

for test_case in range(1, T+1) :
    n = int(input())
    table = [[0 for _ in range(10)] for _ in range(10)]
    purple = 0
    for _ in range(n) :
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1) : # 입력 받은 범위로 2차원 탐색
            for j in range(c1, c2+1) :
                put_color(i, j, color)
                if table[i][j] == 3 : purple += 1 # 이미 보라색이 된 칸은 다시 보라색이 될 일이 없으니 count
    print('#{} {}'.format(test_case, purple))