N, X = map(int, input().split())
A = list(map(int, input().split()))
L = 0
R = N-1
while 1:
    M = (L+R)//2
    if A[M]>X:
        R = M-1
    elif A[M]==X:
        print(M+1)
        break
    else:
        L = M+1