N = int(input())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(N-1):
    G[A[i]-1].append(i+1)
# dp[i]は社員iの部下の数
dp = [0]*N
for i in range(N)[::-1]:
    for g in G[i]:
        dp[i] += dp[g]+1
print(*dp)