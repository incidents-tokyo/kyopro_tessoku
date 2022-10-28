N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [-1]*N
dp[0] = 0
check = [False]*N
check[0] = True
for i in range(N-1):
    if check[i]:
        dp[A[i]-1] = max(dp[A[i]-1], dp[i]+100)
        check[A[i]-1] = True
        dp[B[i]-1] = max(dp[B[i]-1], dp[i]+150)
        check[B[i]-1] = True
print(dp[-1])
'''
かっこいいコード
N=int(input())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
 
dp=[-1]*(N+1)
dp[1]=0
for i in range(N):
    if dp[i]!=-1:
        dp[A[i-1]]=max(dp[A[i-1]],dp[i]+100)
        dp[B[i-1]]=max(dp[B[i-1]],dp[i]+150)
print(dp[-1])
# マイナスが十分に大きければチェックはいらない
'''