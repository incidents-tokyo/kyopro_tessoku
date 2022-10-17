N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [1]*N
for i in range(1,N):
    R[i] = R[i-1]
    while R[i]<N and A[R[i]]-A[i-1]<=K:
        R[i] += 1
ans = 0
for i in range(1,N):
    ans += R[i]-i
print(ans)