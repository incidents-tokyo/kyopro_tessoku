N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(S+1):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+A[i]<=S:
            dp[i+1][j+A[i]] = True
if not dp[N][S]:
    print(-1)
else:
    ans = list()
    i = N
    j = S
    while i>0:
        if j-A[i-1]>=0 and dp[i-1][j-A[i-1]]:
            ans.append(i)
            j -= A[i-1]    
        i -= 1
    print(len(ans))
    print(*ans[::-1])