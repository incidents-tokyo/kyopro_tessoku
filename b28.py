N = int(input())
a, b = 1, 1
mod = 10**9+7
for i in range(N-2):
    a, b = b, (a+b)%mod
print(b)