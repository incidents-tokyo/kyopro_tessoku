N, L = map(int, input().split())
A = [0]*N
B = ['']*N
for i in range(N):
    a, b = input().split()
    A[i], B[i] = int(a), b
ans = 0
for i in range(N):
    if B[i]=='E':
        ans = max(ans, L-A[i])
    if B[i]=='W':
        ans = max(ans, A[i])
print(ans)