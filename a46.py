# 貪欲法
def GetDistance(i, j):
    return ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5

def PlayGreedy():
    CurrentPlace = 0
    visited = [False]*N
    visited[0] = True
    P = [0]

    for i in range(1,N):
        mindist = 10**10
        min_id = -1
        for j in range(N):
            if visited[j]:
                continue
            NewDist = GetDistance(j, CurrentPlace)
            if mindist>NewDist:
                mindist = NewDist
                min_id = j
        visited[min_id] = True
        P.append(min_id)
        CurrentPlace = min_id
    P.append(0)
    return P

N = int(input())
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
answer = PlayGreedy()
for i in answer:
    print(i+1)