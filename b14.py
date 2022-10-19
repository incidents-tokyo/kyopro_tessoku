N, K = map(int, input().split())
A = list(map(int, input().split()))
P = set()
Q = set()
for i in range(2**(N//2)):
    sum_a = 0
    for j in range(N//2):
        if i%2==1:
            sum_a += A[j]
        i = i//2
    P.add(sum_a)
for i in range(2**(N-N//2)):
    sum_a = 0
    for j in range(N//2, N):
        if i%2==1:
            sum_a += A[j]
        i = i//2
    Q.add(sum_a)
for p in P:
    if K-p in Q:
        print("Yes")
        break
else:
    print("No")

