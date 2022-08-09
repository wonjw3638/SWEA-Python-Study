# 1208_Flatten
# 220809

import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    box_list = [0] * 101 # 박스 개수 1개 ~ 100개인데 idx 계산하기 쉽게 101까지
    min_idx , max_idx = 101, -1


    for box in boxes:
        box_list[box] += 1
        if box < min_idx: 
            min_idx = box
        if box > max_idx: 
            max_idx = box

    while dump > 0:
        dump -= 1

        box_list[min_idx] -= 1   # 가장 박스가 적은 곳에 박스 쌓기
        box_list[min_idx + 1] += 1
        if not box_list[min_idx] : 
            min_idx += 1  # 박스 개수 min_idx개 있으면 그대로 이제 없으면 다음 개수로

        box_list[max_idx] -= 1   # 가장 박스가 많은 곳에 박스 빼기
        box_list[max_idx - 1] += 1
        if not box_list[max_idx] : 
            max_idx -= 1  # 박스 개수 min_idx개 있으면 그대로 이제 없으면 다음 개수로

    print('#{} {}'.format(tc, max_idx - min_idx))