import bisect
N = int(input())
A = list(map(int, input().split()))
dp = [-1]*N  # dp[i]は末尾がA[i]のときの最長文字列
INF = 500001
L = [INF]*N  # L[x-1]は長さxの文字列の最小のA
dp[0] = 1
L[0] = A[0]
for i in range(1,N):
    pos = bisect.bisect_left(L, A[i])
    dp[i] = pos+1
    if L[dp[i]-1]>=A[i]:
        L[dp[i]-1] = A[i]
print(max(dp))

