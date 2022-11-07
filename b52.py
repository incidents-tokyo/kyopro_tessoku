from collections import deque
N, X = map(int, input().split())
A = list(input())
Q = deque()
Q.append(X)
A[X-1] = '@'
while len(Q)!=0:
    pos = Q.popleft()
    if pos-2>=0 and A[pos-2]=='.':
        A[pos-2] = '@'
        Q.append(pos-1)
    if pos<=N-1 and A[pos]=='.':
        A[pos] = '@'
        Q.append(pos+1)
print(''.join(A))