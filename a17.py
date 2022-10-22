N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
T = [0]*N
T[1] = A[0]
for i in range(2,N):
    T[i] = min(A[i-1]+T[i-1], B[i-2]+T[i-2])
i = N-1
ans = list()
ans.append(N)
while i!=0:
    if A[i-1]+T[i-1] <= B[i-2]+T[i-2]:
        ans.append(i)
        i = i-1
    else:
        ans.append(i-1)
        i = i-2
print(len(ans))
print(*[i for i in ans[::-1]])