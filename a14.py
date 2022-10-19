def check(Q, num, N):
    L = 0
    R = N-1
    while L<R:
        M = (L+R)//2
        if Q[M]>=num:
            R = M
        else:
            L = M+1
    if Q[L]==num:
        return True
    else:
        return False

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
P = [0]*N**2
Q = [0]*N**2
for i in range(N):
    offset = i*N
    for j in range(N):
        P[offset+j] = A[i]+B[j]
        Q[offset+j] = C[i]+D[j]
Q.sort()
for p in P:
    if check(Q, K-p, N**2):
        print("Yes")
        exit()
print("No")
'''
好きなコード
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=list(map(int,input().split()))
 
Ac=set()
Cd=set()
for i in range(N):
	for j in range(N):
		Ac.add(A[i] + B[j])
		Cd.add(C[i] + D[j])
 
for i in Ac:
	if K-i in Cd:
		print("Yes")
		break
else:
	print("No")
'''