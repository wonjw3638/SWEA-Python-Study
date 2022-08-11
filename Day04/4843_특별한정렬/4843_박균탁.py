
import sys

sys.stdin = open('input.txt','r')
bun = int(input())

def selectionSort(a, N) :
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] < a[j] :
                minIdx = j
        a[minIdx], a[i] = a[i], a[minIdx] 

for he in range(1,bun+1) :
    gilee = int(input())
    baeyul = list(map(int,input().split()))
    print(gilee)    
    selectionSort(baeyul, gilee) # 주어진 숫자 내림차순 배열
    print(baeyul)
    lst = []
    for i in range(gilee):
        if i % 2 ==0 :
            lst.append(baeyul[int(i/2)]) # 최대값 숫자 배열
            
        else :
            lst.append(baeyul[gilee-int((i+1)/2)]) # 최소값 숫자 배열
    print(lst)



     