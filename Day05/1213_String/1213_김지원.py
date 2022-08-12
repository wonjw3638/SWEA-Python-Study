# 1213 - String
# 220812

import sys
sys.stdin = open('input.txt','rt', encoding='UTF8')

for _ in range(1, 11):
    tc = input()
    key = input()
    string = input()

    lenKey = idx = answer = 0

    for _ in key:
        lenKey += 1    # key 길이
        
    for s in string:
        if s == key[idx]:
            if idx == (lenKey - 1):   # key길이만큼 같으면 답 += 1
                answer += 1
                idx = 0
            else:
                idx += 1
        else:
            if s == key[0]:  # key[idx] 값과는 다른데, 다시 key첫 값과 같은 경우
                idx = 1
            else :
                idx = 0
    
    print('#{} {}'.format(tc, answer))