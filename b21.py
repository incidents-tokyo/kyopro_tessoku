N = int(input())
S = input()
dp = [[-1]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    j = i+1
    if S[i]==S[j]:
        dp[i][j] = 2
    else:
        dp[i][j] = 1
for Len in range(N):
    for r in range(Len, N):
        l = r-Len
        if l<N-1 and r>0:
            if S[l]==S[r]:
                dp[l][r] = max(dp[l][r], dp[l+1][r-1]+2, dp[l+1][r], dp[l][r-1])
            else:
                dp[l][r] = max(dp[l][r], dp[l+1][r], dp[l][r-1])
        elif l<N-1:
            dp[l][r] = max(dp[l][r], dp[l+1][r])
        elif r>0:
            dp[l][r] = max(dp[l][r], dp[l][r-1])
print(dp[0][N-1])