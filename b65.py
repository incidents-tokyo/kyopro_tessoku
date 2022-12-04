from collections import deque
N, T = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
reached = [False for _ in range(N)]
d = deque()
d.append(T-1)
reached[T-1] = True

r = deque()     # 帰りがけ
r.append(T-1)   #

while d:
    v = d.pop()  # dはpopされていく
    for i in G[v]:
        if reached[i]: # 頂点iに到達済みであれば無視
            continue
        reached[i] = True
        d.append(i)
        r.append(i)  # 帰りがけ

dp = [-10000000000000000]*N
while r:        # 帰りがけ
    i = r.pop() #
    dp[i] = 0
    for g in G[i]:
        dp[i] = max(dp[i], dp[g]+1)
print(*dp)