N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    L = 0
    R = N-1
    X = int(input())
    while 1:
        M = (L+R)//2
        if A[M]>X:
            R = M-1
            if L>R:
                print(M)
                break
        elif A[M]==X:
            print(M)
            break
        else:
            L = M+1
            if L>R:
                print(M+1)
                break
'''
かっこいいコード
from bisect import bisect_left
 
N = int(input())
A = list(map(int, input().split()))
 
tar = sorted(A)
 
Q = int(input())
for _ in range(Q):
    X = int(input())
    idx = bisect_left(tar, X)
    print(idx)
'''