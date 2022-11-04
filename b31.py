N = int(input())
a = N//3
b = N//5
c = N//7
ab = N//15
bc = N//35
ca = N//21
abc = N//(3*5*7)
print(a+b+c-ab-bc-ca+abc)