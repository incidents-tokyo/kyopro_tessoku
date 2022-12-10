N, C = input().split()
N = int(N)
A = input()
score = 0
for i in range(N):
    if A[i]=='W':
        score += 0
    if A[i]=='R':
        score += 1
    if A[i]=='B':
        score += 2
if C=='W':
    print('Yes' if score%3==0 else 'No')
if C=='R':
    print('Yes' if score%3==1 else 'No')
if C=='B':
    print('Yes' if score%3==2 else 'No')