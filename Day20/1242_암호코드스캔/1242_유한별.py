import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
htb = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
code = {
    (3, 2, 1, 1): '0',
    (2, 2, 2, 1): '1',
    (2, 1, 2, 2): '2',
    (1, 4, 1, 1): '3',
    (1, 1, 3, 2): '4',
    (1, 2, 3, 1): '5',
    (1, 1, 1, 4): '6',
    (1, 3, 1, 2): '7',
    (1, 2, 1, 3): '8',
    (3, 1, 1, 2): '9',
}

# 입력받은 16진수의 table을 2진수 table로 변환
def hex_to_bin(table_row):
    tmp = ''

    for j in range(M):
        tmp += htb.get(table_row[j])
    return tmp


def find_len(table_row, right_idx):
    check = '1'
    cnt = 0
    check_cnt = [0, 1]

    while True:
        if table_row[right_idx] == check: cnt += 1
        else:
            if check_cnt == [2, 2]: break
            if check == '1':
                check = '0'
                check_cnt[0] += 1
            else:
                check = '1'
                check_cnt[1] += 1
            cnt +=1
        right_idx -= 1
    return cnt//7


def code_to_num(table_row, right_idx):
    check = '1'
    idx = 3
    check_cnt = [0, 0, 0, 0]

    while True:
        if table_row[right_idx] != check:
            if not idx: break
            check = '0' if check == '1' else '1'
            idx -= 1
        check_cnt[idx] += 1
        right_idx -= 1
    return check_cnt


def check_code(code_str):
    odd_num = even_num = 0
    for i in range(8):
        if i%2:
            odd_num += int(code_str[i])
        else:
            even_num +=  int(code_str[i])
    if (odd_num*3+even_num)%10:
        return -1
    else:
        return odd_num+even_num


for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = []
    password = set()

    for i in range(N):
        table.append(input())
    
    for i in range(N-1):
        new_table = hex_to_bin(table[i])
        j = M*4-1
        while j >= 0:
            if new_table[j] == '1':
                # n은 password가 몇 배로 늘어나있는지
                n = find_len(new_table, j)
                password.add(new_table[j-(56*n)+1:j+1])
                j -= 56*n
                continue
            j -= 1

    answer = 0
    for p_item in password:
        my_code = ''
        n = len(p_item)//56
        j = 56*n - 1
        while j >= 0:
            tmp = code_to_num(p_item, j)
            for i in range(4):
                tmp[i] //= n
            my_code += code.get(tuple(tmp))
            j -= 7*n
        tmp_answer = check_code(my_code)
        if tmp_answer != -1:
            answer += tmp_answer

    print('#{} {}'.format(tc, answer))