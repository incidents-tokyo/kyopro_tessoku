N = int(input())
A = list(map(int, input().split()))
D = int(input())
l = [0]*(N+2)
r = [0]*(N+2)
for i in range(1, N+1):
    l[i] = max(l[i-1], A[i-1])
    r[N-i+1] = max(r[N-i+2], A[N-i])
for _ in range(D):
    L, R = map(int, input().split())
    print(max(l[L-1], r[R+1]))