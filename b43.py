N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = [0]*N
for i in range(M):
    ans[A[i]-1] += 1
for i in range(N):
    print(M-ans[i])