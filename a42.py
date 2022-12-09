def GetScore(a, b):
    ans = 0
    for i in range(N):
        if a<=A[i]<=a+K and b<=B[i]<=b+K:
            ans += 1
    return ans
N, K = map(int, input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())
ans = 0
for i in range(1, 100-K+1):
    for j in range(1, 100-K+1):
        ans = max(ans, GetScore(i, j))
print(ans)