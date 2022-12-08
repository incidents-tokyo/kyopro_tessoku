X, Y = map(int, input().split())
ans = list()
while X!=1 or Y!=1:
    ans.append((X, Y))
    if X>Y:
        X -= Y
    else:
        Y -= X
print(len(ans))
if len(ans)!=0:
    for x, y in reversed(ans):
        print(x, y)