def compare(list_bin, list_ter):
    num_bin = int(''.join(list_bin), 2)
    num_ter = int(''.join(list_ter), 3)
    if num_bin == num_ter:
        return True
    return False


def xor(c):
    if c == '0':
        return '1'
    else:
        return '0'


T = int(input())

for tc in range(1, T+1):
    bin_input = list(input())
    ter_input = list(input())
    bin_n = len(bin_input)
    ter_n = len(ter_input)
    answer = 0

    for i in range(bin_n):
        bin_input[i] = xor(bin_input[i])
        for j in range(ter_n):
            tmp = ter_input[j]
            for k in range(3):
                if tmp == chr(ord('0')+k):
                    continue
                ter_input[j] = chr(ord('0')+k)
                if compare(bin_input, ter_input):
                    answer = int(''.join(bin_input), 2)
                    break
            ter_input[j] = tmp
        if answer:
            break
        bin_input[i] = xor(bin_input[i])

    print('#{} {}'.format(tc, answer))