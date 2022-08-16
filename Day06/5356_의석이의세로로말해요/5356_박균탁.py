import sys
sys.stdin = open('input.txt','r')
bun = int(input())
def llengthh(a) :
    cnt = 0
    for _ in a:
        cnt += 1
    return cnt
for he in range(1,bun+1) :
    lst = []
    for i in range(5):
        lst.append(input())
    # print(lst)
    max_llen = 0
    for i in lst:
        if max_llen < llengthh(i) :
            max_llen = llengthh(i)
    # print(max_llen)
    ans = []
    for i in range(max_llen):
        for j in range(llengthh(lst)):
            if i < llengthh(lst[j]):
                ans.append(lst[j][i])
    print('#{}'.format(he), end=' ')
    print(''.join(ans))