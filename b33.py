N, H, W = map(int, input().split())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    ans = ans^(A-1)^(B-1)
print('First' if ans!=0 else 'Second')
