N, W = map(int, input().split())
w = [0]*N
v = [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())
dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W+1):
        if dp[i][j]==-1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+w[i]<=W:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])
print(max(dp[N]))
