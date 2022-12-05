from collections import deque
def GetNext(pos, idx):
    State = [0]*N  # ランプiの状態
    for i in range(N):
        State[i] = (pos>>i)&1
    State[X[idx]] = 1 - State[X[idx]]
    State[Y[idx]] = 1 - State[Y[idx]]
    State[Z[idx]] = 1 - State[Z[idx]]

    ret = 0
    for i in range(N):
        if State[i]==1:
            ret += 1<<i
    return ret
N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [0]*M
Y = [0]*M
Z = [0]*M
for i in range(M):
    op = list(map(int, input().split()))
    X[i], Y[i], Z[i] = op[0]-1, op[1]-1, op[2]-1
G = [[] for _ in range(1<<N)]
for i in range(1<<N):
    for j in range(M):
        NextState = GetNext(i, j)
        G[i].append(NextState)

Goal = (1<<N)-1
Start = 0
for i in range(N):
    if A[i]==1:
        Start += 1<<i

Q = deque()
dist = [-1]*(1<<N)
dist[Start] = 0
Q.append(Start)
while Q:
    pos = Q.popleft()
    for next in G[pos]:
        if dist[next]==-1:
            dist[next] = dist[pos]+1
            Q.append(next)
print(dist[Goal])
'''
Bellman-Ford法
全ての辺について
'''