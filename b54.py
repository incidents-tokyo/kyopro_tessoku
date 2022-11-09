N = int(input())
M = {}
ans = 0
for _ in range(N):
    A = int(input())
    if A in M:
        ans += M[A]
        M[A] += 1
    else:
        M[A] = 1
print(ans)