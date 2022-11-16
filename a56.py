def Hash(l,r):
    return (H[r]-B[r-l+1]*H[l-1])%mod  # H[-1]に注意
N, Q = map(int, input().split())
S = input()
S_int = [ord(s)-96 for s in list(S)]
mod = 2147483647
B = [1]*(N+1)
for i in range(1,N+1):
    B[i] = (100*B[i-1])%mod
B[0] = 0
H = [0]*(N+1)
for i in range(N):
    H[i+1] = (S_int[i] + 100*H[i])%mod
for _ in range(Q):
    a,b,c,d = map(int, input().split())
    hash1 = Hash(a,b)
    hash2 = Hash(c,d)
    if hash1==hash2:
        print('Yes')
    else:
        print('No')