import sys
sys.setrecursionlimit(10**7)
def f(x,m):  # 再帰関数は実行時間の影響大
    ans = 1
    for i in range(2,x+1):
        ans = (ans*i)%m
    return ans
def g(a,b,m):  # a**b mod m
    ans=1
    for i in range(30):
        if b%2==1:
            ans = (ans*a)%m
        a, b = (a*a)%m, b//2
    return ans
n, r = map(int, input().split())
M = 10**9+7
N = f(n,M)
R = f(r,M)
NR = f(n-r,M)
R_NR = (R*NR)%M
print((N*g(R_NR,M-2,M))%M)