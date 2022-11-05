N, M = map(int, input().split())
A = [[0]*N for _ in range(M)]
for i in range(M):
    A[i] = list(map(int, input().split()))
INF = 10**9
dp = [[INF]*(1<<N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(1,M+1):   
    for j in range(1<<N):
        # already[k]=1のとき、品物 k は既に無料
        already = [None]*N
        for k in range(N):
            if (j//(1<<k))%2 == 0:
                already[k] = 0
            else:
                already[k] = 1

        # クーポン券 i を選んだ場合の整数表現 v を計算する
        v = 0
        for k in range(N):
            if already[k] == 1 or A[i-1][k] == 1:
                v += (1<<k)

        # 遷移を行う    
        dp[i][v] = min(dp[i][v], dp[i-1][j]+1)
        dp[i][j] = min(dp[i][j], dp[i-1][j])

# 出力
if dp[M][(1<<N)-1] == INF:
    print("-1")
else:
    print(dp[M][(1<<N)-1])
'''
書き換え
for i in range(1,M+1):   
    for S in range(1<<N):
        v = 0
        for t in range(N):
            v |= (A[i-1][t] << t)
        v = S | v
        # 遷移を行う    
        dp[i][v] = min(dp[i][v], dp[i-1][S]+1)
        dp[i][S] = min(dp[i][S], dp[i-1][S])
'''