import heapq
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A-1].append((B-1, C))
    G[B-1].append((A-1, C))
INF = 20000000000
cur = [INF]*N
kakutei = [False]*N

cur[0] = 0
T = []
heapq.heappush(T, (cur[0], 0))
while T:
    pos = heapq.heappop(T)[1]
    if kakutei[pos]:
        continue

    kakutei[pos] = True
    for g in G[pos]:
        next = g[0]
        cost = g[1]
        if cur[next] > cur[pos]+cost:
            cur[next] = cur[pos]+cost
            heapq.heappush(T, (cur[next], next))

Ans = []
pos = N-1
cost =  cur[pos]
Ans.append(pos+1)
while cost!=0:
    for g in G[pos]:
        prev = g[0]
        p_cost = g[1]
        if cur[prev] == cost-p_cost:
            Ans.append(prev+1)
            pos = prev
            cost -= p_cost
print(*Ans[::-1])