N, D = map(int, input().split())
work = list()
for _ in range(N):
    X, Y = map(int, input().split())
    work.append((X-1, Y))
used = [False for _ in range(N)]
ans = 0
for i in range(D):
    maxValue = 0
    maxID = -1
    for j in range(N):
        if used[j]==True:
            continue
        if maxValue < work[j][1] and work[j][0] <= i:
            maxValue = work[j][1]
            maxID = j
    if maxID != -1:
        ans += maxValue
        used[maxID] = True
print(ans)
'''
参考
from collections import deque
import heapq

N,D = map(int,input().split())

G = [list() for _ in range(2001)]

for _ in range(N):
    X,Y = map(int,input().split())
    G[X].append(Y)
    
Q = []
Ans = 0

for i in range(1,D+1):
    for j in G[i]:
        heapq.heappush(Q,-j)
    
    if Q:
        Ans -= heapq.heappop(Q)
     
        
print(Ans)
'''