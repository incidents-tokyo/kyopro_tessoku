N, K = map(int, input().split())
S = input()
on = 0
for s in S:
    if s=='1':
        on += 1
if (on - K)%2==0:
    print('Yes')
else:
    print('No')