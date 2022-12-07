N, K = map(int, input().split())
if (N-1)*2<=K and (K-(N-1)*2)%2==0:
    print('Yes')
else:
    print('No')