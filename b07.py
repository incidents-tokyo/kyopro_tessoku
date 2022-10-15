T = int(input())
N = int(input())
B = [0]*(T+1)
for _ in range(N):
    L, R = map(int, input().split())
    B[L] += 1
    B[R] -= 1
cnt = 0
for i in range(T):
    cnt += B[i]
    print(cnt)