import sys
sys.stdin = open('input.txt', 'r')

# max 값의 idx와 min 값의 idx를 찾아 return
def find_idx(boxes) :
    max_box = boxes[0]
    min_box = boxes[0]
    max_idx, min_idx = 0, 0

    for idx, box in enumerate(boxes) :
        if max_box < box :
            max_box = box
            max_idx = idx
        if min_box > box :
            min_box = box
            min_idx = idx

    return max_idx, min_idx

T = 10

for test_case in range(1, T+1) :
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    while dump > 0 : #
        max_idx, min_idx = find_idx(boxes)
        if boxes[max_idx] - boxes[min_idx] > 1 :
            boxes[max_idx] -= 1
            boxes[min_idx] += 1
            dump -= 1
        else :
            break
    
    max_idx, min_idx = find_idx(boxes)
    print('#{} {}'.format(test_case, boxes[max_idx] - boxes[min_idx]))