from collections import deque
S = input()
D = deque()
for i in range(len(S)):
    if S[i]=='(':
        D.append(i+1)
    else:
        j = D.pop()
        print(j, i+1)