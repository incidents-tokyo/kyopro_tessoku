from collections import deque
N, M = map(int, input().split())
count = [-1]*N
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
Q = deque()
Q.append(0)
count[0]=0
while Q:
    now = Q.popleft()
    for g in G[now]:
        if count[g]==-1:
            count[g] = count[now]+1
            Q.append(g)
for c in count:
    print(c)