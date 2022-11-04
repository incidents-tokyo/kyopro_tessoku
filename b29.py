a, b = map(int, input().split())
mod = 10**9+7
ans = 1
for i in range(128):
    flag = b%2
    if flag:
        ans = (ans*a)%mod
    a = (a*a)%mod  # ここでa=a*aとすると大きい数になり、TLE
    b = b//2
print(ans)