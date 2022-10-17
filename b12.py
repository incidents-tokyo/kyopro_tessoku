def check(x, N):
    x = x/10**4
    if x**3+x >= N:
        return True
    else:
        return False
N = int(input())  # 0<=N<=10**5
L = 0
R = 10**9
while L<R:
    M = (L+R)//2
    if check(M, N):
        R = M 
    else:
        L = M+1
print(L/10**4)