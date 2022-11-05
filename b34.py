N, X, Y = map(int, input().split())  # X, Y = 2, 3
A = list(map(int, input().split()))
# grundy = [0,0,1,1,2,0,0,1,1,2, ... ]
ans = 0
for a in A:
    g = a%5
    if g==2 or g==3:
        ans ^= 1
    elif g==4:
        ans ^= 2
print('First' if ans!=0 else 'Second')