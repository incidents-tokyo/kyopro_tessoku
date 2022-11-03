N = int(input())
num = [True for i in range(N+1)]
num[0] = False
num[1] = False
i = 2
while i*i<=N:
    x = i+i
    while x<=N:
        num[x] = False
        x += i
    i += 1
    while not num[i]:
        i += 1
for i in range(N+1):
    if num[i]:
        print(i)
'''
かっこいいコード
n = int(input())
p=[True]*(n+1)
for i in range(2,n+1):
    if p[i]:
        for j in range(2*i,n+1,i):
            p[j]=False
 
for i in range(2,n+1):
    if p[i]:
        print(i)
'''
