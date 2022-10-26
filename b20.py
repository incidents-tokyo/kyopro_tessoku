S = input()
T = input()
s, t = len(S), len(T)
INF = 2<<30
dp = [[INF]*(t+1) for _ in range(s+1)]
dp[0][0] = 0
for i in range(s+1):
    for j in range(t+1):
        if i>0 and j>0:
            if S[i-1]!=T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        if i>0:
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        if j>0:
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
print(dp[s][t])
'''
a20.pyの参考コード
S = input()
T = input()
s, t = len(S), len(T)
dp = [[0]*(t+1) for _ in range(s+1)]
for i in range(s):
    for j in range(t):
        if S[i]==T[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
print(dp[s][t])
'''