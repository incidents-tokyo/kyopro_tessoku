# 局所探索法 PyPy
from random import randint
import sys
sys.setrecursionlimit(10**7)
def GetDistance(i, j):
    return ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5
def GetScore(L):
    sum = 0
    for i in range(N):
        sum += GetDistance(L[i], L[i+1])
    return sum
def GetNeighbor():
    i, j = 0, 0
    while i==j:
        i = randint(1, N-1)
        j = randint(1, N-1)
    if i>j:
        i, j = j, i
    return i, j
def LocalSearch():
    global P
    CurrentScore = GetScore(P)
    for _ in range(40000):
        L, R = GetNeighbor()
        Q = P[:L]+P[L:R+1][::-1]+P[R+1:]
        NewScore = GetScore(Q)
        if CurrentScore>NewScore:
            P = Q[:]
            CurrentScore=NewScore

N = int(input())
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
# 初期解生成
P = [i for i in range(N)]
P.append(0)
LocalSearch()
for p in P:
    print(p+1)