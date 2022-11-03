def gcd(x,y):
    if x>0 and y>0:
        if x>=y:
            return gcd(y,x%y)
        else:
            return gcd(x,y%x)
    else:
        if x==0:
            return y
        else:
            return x
A, B = map(int, input().split())
print(gcd(A,B))
'''
かっこいいコード
A, B = map(int, input().split())
while B != 0:
    A, B = B, A % B
print(A)
'''