N = int(input())
movie = list()
for _ in range(N):
    L, R = map(int, input().split())
    movie.append((L, R))
movie.sort(key=lambda x: x[1])
ans = 1
time = movie[0][1]
for i in range(1,N):
    if time <= movie[i][0]:
        ans += 1
        time = movie[i][1]
print(ans)