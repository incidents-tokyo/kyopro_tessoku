import sys
sys.setrecursionlimit(10**7)
def dfs(pos):
    visited[pos-1] = True
    for next in G[pos-1]:
        if visited[next-1]==False:
            dfs(next)
N, M = map(int, input().split())
G = [list() for _ in range(N)]
E = [list(map(int, input().split())) for _ in range(M)]
for A, B in E:
    G[A-1].append(B)
    G[B-1].append(A)
visited = [False]*(N)
dfs(1)
Ans = 'The graph is connected.'
for i in range(N):
    if visited[i]==False:
        Ans = 'The graph is not connected.'
        break
print(Ans)
# どうしてもTLE
# PyPyだとダメ, Pythonだといける
# なぜ
'''
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    G[A].append(B)
    G[B].append(A)

stack = [0]
seen = [False] * (N)
seen[0] = True
while stack:
    v = stack.pop()
    for next_v in G[v]:
        if seen[next_v]:
            continue
        seen[next_v] = True
        stack.append(next_v)

ans = "The graph is connected."
for n in range(N):
    if not seen[n]:
        ans = "The graph is not connected."
        break

print(ans)
'''