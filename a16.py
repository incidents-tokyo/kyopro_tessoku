N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [0]*N
dp[1] = A[0]
for i in range(2,N):
    dp[i] = min(A[i-1]+dp[i-1], B[i-2]+dp[i-2])
print(dp[-1])