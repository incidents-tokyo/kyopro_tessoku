import heapq
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A-1].append((B-1,C))
    G[B-1].append((A-1,C))
kakutei = [False]*N
INF = 2000000000
cur = [INF]*N

cur[0] = 0
T = []
heapq.heappush(T,(cur[0],0))
while len(T)!=0:
    pos = heapq.heappop(T)[1]
    if kakutei[pos]==True:
        continue

    kakutei[pos] = True
    for g in G[pos]:
        next = g[0]
        cost = g[1]
        if cur[next]>cur[pos]+cost:
            cur[next] = cur[pos]+cost
            heapq.heappush(T,(cur[next],next))
'''
while True:
    # 操作A: 未確定頂点の中でcurの値が最も小さい頂点posを求める
    pos = -1
    MinDist = INF
    for i in range(N):
        if kakutei[i]==True or MinDist<=cur[i]:
            continue
        pos = i
        MinDist = cur[i]
    # すべて確定しているなら終わり
    if pos==-1:
        break

    # 操作B: posに隣接する頂点について, curの値を更新する
    kakutei[pos] = True
    for g in G[pos]:
        next = g[0]
        cost = g[1]
        cur[next] = min(cur[next], cur[pos] + cost)
'''
for i in range(N):
    if cur[i]==INF:
        print(-1)
    else:
        print(cur[i])