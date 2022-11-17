N, Q = map(int, input().split())
dp = [[0]*N for i in range(31)]
A = list(map(int, input().split()))
for i in range(N):
    dp[0][i] = A[i]-1
for i in range(1,31):
    for j in range(N):
        dp[i][j] = dp[i-1][dp[i-1][j]]
for _ in range(Q):
    X, Y = map(int, input().split())
    ans = X-1
    i=0
    while Y>0:
        if Y%2==1:
            ans = dp[i][ans]
        Y = Y//2
        i+=1
    print(ans+1)