S = 1500
N = int(input())
grid = [[0]*(S+2) for _ in range(S+2)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    grid[A][B] += 1
    grid[A][D] -= 1
    grid[C][B] -= 1
    grid[C][D] += 1
for i in range(S+2):
    for j in range(1, S+2):
        grid[i][j] += grid[i][j-1]
for i in range(1, S+2):
    for j in range(S+2):
        grid[i][j] += grid[i-1][j]
ans = 0
for i in range(S+1):
    for j in range(S+1):
        if grid[i][j] > 0:
            ans += 1
print(ans)
'''
座標か空間か
'''