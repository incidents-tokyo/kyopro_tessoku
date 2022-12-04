# Union-Find 木
class unionfind:
    # n 頂点の Union-Find 木を作成
    def __init__(self, n):
        self.n = n
        self.par = [-1]*n  # 最初は親が無い
        self.size = [1]*n  # 最初はグループの頂点数が 1
    
    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
    
    # 要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)
# 入力
N, M = map(int, input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())
Q = int(input())
type = [0]*Q
x = [0]*Q
u = [0]*Q
v = [0]*Q
for i in range(Q):
    query = list(map(int, input().split()))
    type[i] = query[0]
    if type[i]==1:
        x[i] = query[1]
    elif type[i]==2:
        u[i] = query[1]
        v[i] = query[2]
# 運休になる路線を求める
cancelled = [False for _ in range(M)]
for i in range(Q):
    if type[i]==1:
        cancelled[x[i]] = True
# Union-Find の初期化（その日の最後の状態にする）
uf = unionfind(N)
for i in range(M):
    if cancelled[i]==False and uf.same(A[i], B[i])==False:
        uf.unite(A[i], B[i])
# クエリを逆から処理
ans = ['' for _ in range(Q)]
for i in range(Q)[::-1]:
    if type[i]==1:
        if uf.same(A[x[i]], B[x[i]])==False:
            uf.unite(A[x[i]], B[x[i]])
    if type[i]==2:
        if uf.same(u[i], v[i])==True:
            ans[i] = 'Yes'
        else:
            ans[i] = 'No'
# 出力
for i in range(Q):
    if type[i]==2:
        print(ans[i])