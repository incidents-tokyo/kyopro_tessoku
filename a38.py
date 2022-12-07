D, N = map(int, input().split())
LIM = [24]*D
for _ in range(N):
    L, R, H = map(int, input().split())
    for i in range(L-1, R):
        LIM[i] = min(LIM[i], H)
print(sum(LIM))