N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B)
    G[B-1].append(A)
ans = [1, len(G[0])]
for i in range(1,N):
    if ans[1] < len(G[i]):
        ans = [i+1, len(G[i])]
print(ans[0])
'''
数だけ考える
    N, M = map(int, stdin.readline().split())
    friend_count = [0]*N
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        friend_count[A-1] += 1
        friend_count[B-1] += 1
    max_val = max(friend_count)
    print(friend_count.index(max_val)+1)
'''