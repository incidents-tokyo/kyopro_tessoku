A, B = map(int, input().split())
ans = "No"
for i in range(A,B+1):
    if 100%i == 0:
        ans = "Yes"
print(ans)