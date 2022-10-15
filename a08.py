H, W = map(int, input().split())
X = list()
X.append([0]*(W+1))
for _ in range(H):
    X.append([0]+list(map(int, input().split())))
for i in range(H+1):
    for j in range(1, W+1):
        X[i][j] = X[i][j-1] + X[i][j]
for j in range(W+1):
    for i in range(1, H+1):
        X[i][j] = X[i-1][j] + X[i][j]
Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(X[C][D]-X[C][B-1]-X[A-1][D]+X[A-1][B-1])
'''
かっこいいコード
h, w = map(int, input().split())
grid = [[0] * (w+1)] + [[0] + list(map(int, input().split())) for _ in range(h)]
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
 
for y in range(h):
    for x in range(w):
        grid[y+1][x+1] = grid[y+1][x] + grid[y][x+1] + grid[y+1][x+1] - grid[y][x]
        
for a, b, c, d in query:
    print(grid[c][d] - grid[a-1][d] - grid[c][b-1] + grid[a-1][b-1])
'''