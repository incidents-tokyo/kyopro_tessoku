N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
for i in range(N):
    if A[i] == 1:
        S[i+1] = S[i] + 1
    else:
        S[i+1] = S[i] - 1
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    flag = S[R] - S[L-1]
    if flag > 0:
        print("win")
    elif flag == 0:
        print("draw")
    else:
        print("lose")
