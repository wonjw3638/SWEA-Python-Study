# 4366 정식이의 은행업무
# 220920

'''
10:30~10:54
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    bina = input()
    trit = input()
    bina_list = list()

    # 2진수를 10진수로 변환
    btod = 0
    for idx in range(len(bina)):
        if bina[-1*(idx+1)] == '1':
            btod += 2**idx

    for idx in range(len(bina)):
        if bina[-1*(idx+1)] == '1':
            bina_list.append(btod-(2**idx))
        else:
            bina_list.append(btod+(2**idx))

    # 3진수를 10진수로 변환
    ttod = 0
    for idx in range(len(trit)):
        if trit[-1*(idx+1)] == '1':
            ttod += 3**idx
        elif trit[-1*(idx+1)] == '2':
            ttod += (3**idx)*2
        else:
            continue

    for idx in range(len(trit)):
        if trit[-1*(idx+1)] == '1':
            tmp = ttod - (3**idx)
            if tmp in bina_list:
                answer = tmp
                break
            
            tmp = ttod + (3**idx)
            if tmp in bina_list:
                answer = tmp
                break

        elif trit[-1*(idx+1)] == '2':
            tmp = ttod - (3**idx)
            if tmp in bina_list:
                answer = tmp
                break
            
            tmp = ttod - 2 * (3**idx)
            if tmp in bina_list:
                answer = tmp
                break
        
        else:
            tmp = ttod + (3**idx)
            if tmp in bina_list:
                answer = tmp
                break
            
            tmp = ttod + 2*(3**idx)
            if tmp in bina_list:
                answer = tmp
                break

    print('#{} {}'.format(tc, answer))