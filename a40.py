N = int(input())
A = list(map(int, input().split()))
count = [0]*100
for a in A:
    count[a-1] += 1
ans = 0
for c in count:
    ans += c*(c-1)*(c-2)//6
print(ans)