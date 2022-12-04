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
N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
E.sort(key=lambda x: -x[2])
ans = 0
uf = unionfind(N)
for A, B, C in E:
    A -= 1
    B -= 1
    if uf.same(A, B):
        continue
    uf.unite(A, B)
    ans += C
print(ans)