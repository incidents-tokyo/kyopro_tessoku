N, W = map(int, input().split())
w = [0]*N
v = [0]*N
max_v = 10**5
INF = 10**12
for i in range(N):
    w[i], v[i] = map(int, input().split())
dp = [[INF]*(max_v+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(max_v+1):
        if dp[i][j]==INF:
            continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+v[i]<=max_v:
            dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j]+w[i])
ans = 0
for i in range(1,max_v+1):
    if dp[N][i]<=W:
        ans = max(ans, i)
print(ans)
'''
一次元配列
n, W = map(int, input().split())
inf = 1 << 60
V = 100100
dp = [inf] * V
dp[0] = 0
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(V - 1, v - 1, -1):
        dp[i] = min(dp[i], dp[i - v] + w)
 
ans = 0
for i in range(V):
    if dp[i] <= W:
        ans = i
print(ans)
'''