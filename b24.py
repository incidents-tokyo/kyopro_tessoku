import bisect
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort(key=lambda x: (x[1], -x[0]))  # x[1]が同じならx[0]が大きいほうを前に
dp = [0]*N  # dp[i]はX[i][0]が一番大きくなるときの最小の重なり
INF = 10**10
L = [INF]*N  # L[x-1]は長さxとなるX[i][0]の中で一番小さい
dp[0] = 1
L[0] = XY[0][0]
for i in range(1,N):
    pos = bisect.bisect_left(L,XY[i][0])
    dp[i] = pos+1
    L[dp[i]-1] = min(L[dp[i]-1], XY[i][0])
print(max(dp))