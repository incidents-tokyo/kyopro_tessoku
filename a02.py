import sys
N, X = map(int, input().split())
A = list(map(int, input().split()))
for item in A:
    if item == X:
        print("Yes")
        sys.exit()
print("No")

'''
他の人のかっこいいソースコード
N,X=input().split();print("YNeos"[X not in input().split()::2])
こういうのが書きたかった
N, X = map(int, input().split())
A = list(map(int, input().split()))
 
if X in A:
    print('Yes')
else:
    print('No')
'''