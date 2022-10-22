INF = 10**10
N = int(input())
h = list(map(int, input().split()))
dp = [INF]*N
dp[0] = 0
for i in range(N):
    if N-(i+1)>0:
        dp[i+1] = min(abs(h[i]-h[i+1])+dp[i], dp[i+1])
    if N-(i+2)>0:
        dp[i+2] = min(abs(h[i]-h[i+2])+dp[i], dp[i+2])
i = N-1
ans = list()
ans.append(i+1)
while i>0:
    if i==1:
        ans.append(1)
        break
    else:
        if abs(h[i]-h[i-1])+dp[i-1]==dp[i]:
            i = i-1
            ans.append(i+1)
        else:
            i = i-2
            ans.append(i+1)
print(len(ans))
print(*ans[::-1])
'''
よいコード
INF = 1<<60
'''