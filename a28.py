N = int(input())
ans = 0
for _ in range(N):
    T, A = input().split()
    A = int(A)
    if T=='+':
        ans = (ans+A)%10000
    elif T=='-':
        ans = (ans-A)%10000
    elif T=='*':
        ans = (ans*A)%10000
    print(ans)