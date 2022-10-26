N = int(input())
P = [0]*N
A = [0]*N
for i in range(N):
    P[i], A[i] = map(int, input().split())
dp = [[0]*N for _ in range(N)]
for Len in range(N-1)[::-1]:  # N-2~0
    for l in range(N-Len):  #0~N-Len-1
        r = l+Len
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
P = [0]*N
A = [0]*N
for i in range(N):
    P[i], A[i] = map(int, input().split())
dp = [[0]*N for _ in range(N)]
for Len in range(N-1)[::-1]:  # N-2~0
    for l in range(N-Len):  #0~N-Len-1
        r = l+Len
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