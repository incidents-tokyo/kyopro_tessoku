N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
print(sum(A)*M+B*N*M+sum(C)*N)