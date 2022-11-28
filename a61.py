N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B)
    G[B-1].append(A)
for i in range(N):
    ans = ''
    for g in G[i]:
        ans += str(g)+','
    print(str(i+1) + ': {' + ans[:-1] +'}')
'''
かっこいいコード
n, m = map(int, input().split())
d = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    d[a-1].append(str(b))
    d[b-1].append(str(a))
 
for i in range(n):
    print(str(i+1)+": {"+','.join(d[i])+"}")
'''