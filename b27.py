a,b = map(int, input().split())
A,B = a,b
while B!=0:
    A,B = B,A%B
print(a*b//A)