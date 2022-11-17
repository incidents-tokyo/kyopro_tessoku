N, K = map(int, input().split())
# dp[i][j] : jに対して2^i回行った後の数
dp = [[0]*(N+1) for _ in range(30)]
for i in range(N+1):
    num = str(i)
    dp[0][i] = i
    for j in num:
        dp[0][i] -= ord(j)-ord('0')
for i in range(1,30):
    for j in range(N+1):
        dp[i][j] = dp[i-1][dp[i-1][j]]
for i in range(1,N+1):
    k = K
    ans = i
    j = 0
    while k>0:
        if k%2==1:
            ans = dp[j][ans]
        j += 1
        k = k//2
    print(ans)