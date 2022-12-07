N = int(input())
S = input()
LIM1 = [1]*N
LIM2 = [1]*N
for i in range(N-1):
    if S[i]=='A':
        LIM1[i+1] = LIM1[i]+1
for i in reversed(range(N-1)):
    if S[i]=='B':
        LIM2[i] = LIM2[i+1]+1
G = [0]*N
for i in range(N):
    G[i] = max(LIM1[i], LIM2[i])
print(sum(G))