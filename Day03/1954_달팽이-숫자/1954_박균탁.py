import sys
sys.stdin = open('input.txt','r')
bun = int(input())
for he in range(1,bun+1) :
    test = int(input())
    
    square = [[0] * test for _ in range(test)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] # 방향 우하좌상
    x, y = 0, 0 # 좌표 정보
    way = 0

    for i in range(1, test**2+1) :
        square[x][y] = i # 리스트에 숫자 넣기
        x += dx[way]     # x축 방향설정
        y += dy[way]     # y축 방향설정
         # dx, dy에 따른 방향 설정
        if not 0 <= x < test or not 0 <= y < test or square[x][y] != 0 :
            x -= dx[way]
            y -= dy[way]
            way = (way + 1) % 4
            x += dx[way]
            y += dy[way]

    print('#{}' .format(he))
    for j in range(test) :
        for k in range(test) :
            print(square[j][k], end=' ')
        print()