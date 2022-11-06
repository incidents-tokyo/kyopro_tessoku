N = int(input())
A = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[N-1][i] = A[i]
if (N-1)%2==1:
    taro = True
else:
    taro = False
edge = 0
for i in reversed(range(N-1)):
    edge += 1
    for j in range(N-edge):
        if taro:
             dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])
    taro = not taro
print(dp[0][0])