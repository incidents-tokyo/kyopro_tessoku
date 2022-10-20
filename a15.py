def pos(s, num, size):
    L = 0
    R = size-1
    while L<R:
        M = (L+R)//2
        if s[M]>=num:
            R = M
        else:
            L = M+1
    return L+1
N = int(input())
A = list(map(int, input().split()))
S = list(set(A))
S.sort()
ans = ""
for i in range(N):
    ans += str(pos(S,A[i],len(S)))+" "
print(ans)
'''
かっこいいコード
n = int(input())
a = list(map(int, input().split()))
 
b = sorted(set(a))
c = {}
for i in range(len(b)):
    c[b[i]] = i + 1
 
print(' '.join([str(c[a[i]]) for i in range(n)]))
知っておくべき書き方
print(*[c[i] for i in a])
'''
