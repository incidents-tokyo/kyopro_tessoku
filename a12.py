def check(A, x, K):
    sum_p = 0
    for a in A:
        sum_p += x//a
    if sum_p>=K:
        return True
    else:
        return False
N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 1
R = 10**9
while L<R:
    M = (L+R)//2
    if check(A, M, K):
        R = M
    else:
        L = M+1
print(L)