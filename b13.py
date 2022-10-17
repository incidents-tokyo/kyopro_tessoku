N, K = map(int, input().split())
A = list(map(int, input().split()))+[0]
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = A[i-1] + S[i-1]
R = [1]*(N+1)
for i in range(1,N+1):
    R[i] = R[i-1]
    while R[i]<N+1 and S[R[i]]-S[i-1]<=K:
        R[i] += 1
ans = 0
for i in range(1,N+1):
    ans += R[i]-i
print(ans)