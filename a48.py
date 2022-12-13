# 焼きなまし法
from random import randint, random
from math import exp
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
def Annealing():
    global P
    CurrentScore = GetScore(P)
    for t in range(40000):
        L, R = GetNeighbor()
        Q = P[:L]+P[L:R+1][::-1]+P[R+1:]
        NewScore = GetScore(Q)
        T = 30-28*t/40000
        Prob = exp(min(0, (CurrentScore-NewScore)/T))
        if random()<Prob:
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
Annealing()
for p in P:
    print(p+1)