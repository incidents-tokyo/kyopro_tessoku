INF = 10**9
N = int(input())
h = list(map(int, input().split()))
dp = [INF]*N
dp[0] = 0
for i in range(N):
    if N-(i+1)>0:
        dp[i+1] = min(abs(h[i]-h[i+1])+dp[i], dp[i+1])
    if N-(i+2)>0:
        dp[i+2] = min(abs(h[i]-h[i+2])+dp[i], dp[i+2])
print(dp[-1])
'''
かっこいいコード
N = int(input())
h = list(map(int,input().split()))
dp = [0]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])
for i in range(2,N):
  dp[i] = min(dp[i-1]+abs(h[i-1]-h[i]),dp[i-2]+abs(h[i-2]-h[i]))
print(dp[N-1])
'''