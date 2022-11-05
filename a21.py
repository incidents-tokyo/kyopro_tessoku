N = int(input())
P = [0]*N
A = [0]*N
for i in range(N):
    P[i], A[i] = map(int, input().split())
dp = [[0]*N for _ in range(N)]
for Len in range(N-1)[::-1]:  # N-2~0: 区間の長さ
    for l in range(N-Len):  #0~N-Len-1: 区間の始点
        r = l+Len  # 区間の終点
        score1, score2 = 0, 0
        if l>0 and l<=P[l-1]-1<=r:
            score1 = A[l-1]
        if r<N-1 and l<=P[r+1]-1<=r:
            score2 = A[r+1]
        if l==0:
            dp[l][r] = max(dp[l][r], dp[l][r+1]+score2)
        elif r==N-1:
            dp[l][r] = max(dp[l][r], dp[l-1][r]+score1)
        else:
            dp[l][r] = max(dp[l][r], dp[l-1][r]+score1, dp[l][r+1]+score2)
ans = 0
for i in range(N):
    ans = max(ans, dp[i][i])
print(ans)
'''
かっこいいコード
N = int(input())
P = [0]
A = [0]
for i in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [[0] * (N + 2) for _ in range(N + 2)]
for l in range(1, N + 1):
    for r in reversed(range(l, N + 1)):
        l_score, r_score = 0, 0
        if l != 1 and l <= P[l - 1] <= r:
            l_score = A[l - 1]

        if r != N and l <= P[r + 1] <= r:
            r_score = A[r + 1]

        dp[l][r] = max(dp[l - 1][r] + l_score, dp[l][r + 1] + r_score)


ans = 0
for i in range(0, N + 2):
    ans = max(ans, dp[i][i])

print(ans)
'''