N = int(input())
A = list(map(int, input().split()))
mod = [0]*100
ans = 0
for a in A:
    div = a%100
    if div==0 or div==50:
        ans += mod[div]
    else:
        ans += mod[100-div]
    mod[div] += 1
print(ans)