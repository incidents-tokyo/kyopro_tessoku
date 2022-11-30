N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
stack = [0]
visited = [False]*N
visited[0] = True
prev = [-1]*N
while stack:
    v = stack.pop()
    for next_v in G[v]:
        if visited[next_v]:
            continue
        visited[next_v] = True
        prev[next_v] = v
        stack.append(next_v)
ans = []
start = N-1
while prev[start] != -1:
    ans.append(start)
    start = prev[start]
ans.append(0)
for i in range(len(ans) - 1, -1, -1):
    print(ans[i] + 1, end=' ')
print()