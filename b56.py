def Hash_f(l,r):
    return (H_f[r]-B[r-l+1]*H_f[l-1])%mod
def Hash_b(l,r):
    return (H_b[r]-B[r-l+1]*H_b[l-1])%mod
N, Q = map(int, input().split())
S = list(input())
S_int = [ord(s)-96 for s in S]
mod = 2147483647
H_f = [0]*(N+1)
H_b = [0]*(N+1)
for i in range(1,N+1):
    H_f[i] = (S_int[i-1]+100*H_f[i-1])%mod
for i in range(1,N+1):
    H_b[i] = (S_int[N-i]+100*H_b[i-1])%mod
B = [1]*(N+1)
for i in range(1,N+1):
    B[i] = (100*B[i-1])%mod
B[0] = 0
for _ in range(Q):
    L, R = map(int, input().split())
    hash_f = Hash_f(L,R)
    hash_b = Hash_b(N-R+1,N-L+1)
    if hash_f == hash_b:
        print('Yes')
    else:
        print('No')