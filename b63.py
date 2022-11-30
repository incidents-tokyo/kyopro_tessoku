from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
G = [[] for _ in range(R*C)]
for i in range(R):
    grid = input()
    for j in range(C):
        pos = i*C+j
        if grid[j]=='#':
            G[pos].append(-1)
            continue
        if j>=1 and grid[j-1]=='.':
            G[pos].append(pos-1)
            G[pos-1].append(pos)
        if i>=1 and -1 not in G[pos-C]:
            G[pos].append(pos-C)
            G[pos-C].append(pos)
Q = deque()
count = [-1]*(R*C)
start = (sy-1)*C+sx-1
goal = (gy-1)*C+gx-1
Q.append(start)
count[start] = 0
while Q:
    now = Q.popleft()
    for g in G[now]:
        if count[g]==-1:
            count[g] = count[now]+1
            Q.append(g)
print(count[goal])