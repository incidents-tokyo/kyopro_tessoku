import math
N = int(input())
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
G = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        G[i][j] = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
        G[j][i] = G[i][j]
INF = 10**9
dp = [[INF]*N for _ in range(1<<N)]
dp[0][0] = 0
for S in range(1<<N):
    for v in range(N):
        for u in range(N):
            if not (S>>u)&1 and S!=0:
                continue
            if (S>>v)&1==0:
                dp[S|(1<<v)][v] = min(dp[S|(1<<v)][v], dp[S][u]+G[u][v])
if dp[(1<<N)-1][0] != INF:
    print(dp[(1<<N)-1][0])
else:
    print(-1)