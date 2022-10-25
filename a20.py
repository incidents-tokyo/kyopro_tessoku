S = input()
T = input()
dp = [[0]*(len(S)+1) for _ in range(len(T)+1)]
for i in range(len(T)+1):
    for j in range(len(S)+1):
        if i>0 and j>0 and S[j-1]==T[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
        elif i>0 and j>0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif j>0:
            dp[i][j] = dp[i][j-1]
        elif i>0:
            dp[i][j] = dp[i-1][j]
print(dp[len(T)][len(S)])
'''
かっこいいコード
S = input()
T = input()
n,m = len(S),len(T)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
  for j in range(m):
    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    if S[i] == T[j]:
      dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+1)
print(dp[n][m])
'''