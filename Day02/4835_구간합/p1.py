T = int(input())
for i, _ in enumerate(range(T), start=1):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_diff = 0
    for num_a in num_list:
        for num_b in num_list:
            if max_diff <= num_a - num_b:
                max_diff = num_a - num_b

    print('#{} {}'.format(i, max_diff))