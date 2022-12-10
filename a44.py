N, Q = map(int, input().split())
A = [i+1 for i in range(N)]
State=0
for _ in range(Q):
    query = list(map(int, input().split()))
    Type = query[0]
    if Type==1:
        x, y = query[1], query[2]
        if State==0:
            A[x-1] = y
        else:
            A[N-x] = y
    elif Type==2:
        State = 1 - State
    elif Type==3:
        x = query[1]
        if State==0:
            print(A[x-1])
        else:
            print(A[N-x])