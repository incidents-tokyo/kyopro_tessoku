from collections import deque
N = int(input())
A = list(map(int, input().split()))
Level2 = deque()
Ans = []
for i in range(N):
    if i>=1:
        Level2.append((i,A[i-1]))
        while(len(Level2)!=0):
            kabuka = Level2[-1][1]
            if kabuka<=A[i]:
                Level2.pop()
            else:
                break
    if len(Level2)!=0:
        Ans.append(Level2[-1][0])
    else:
        Ans.append(-1)
print(*Ans)