N = int(input())
grid = [[0]*1501 for _ in range(1501)]
for _ in range(N):
    X, Y = map(int, input().split())
    grid[X][Y] += 1
for i in range(1501):
    for j in range(1, 1501):
        grid[i][j] = grid[i][j-1] + grid[i][j]
for j in range(1501):
    for i in range(1, 1501):
        grid[i][j] = grid[i-1][j] + grid[i][j]
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(grid[c][d]-grid[c][b-1]-grid[a-1][d]+grid[a-1][b-1])