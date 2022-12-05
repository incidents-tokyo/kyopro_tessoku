# 参考
# 最大フロー用の辺の構造体
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

# 深さ探索
def dfs(pos, goal, F, G, used):
    if pos==goal:
        return F  # ゴールに到着:フローを流せる!
    # 探索する
    used[pos] = True
    for e in G[pos]:
        # 容量が1以上かつ、まだ訪問していない頂点にのみ行く
        if e.cap>0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            # フローを流せる場合、残余グラフの容量をflowだけ増減させる
            if flow>=1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    # すべての辺を探索しても見つからなかった
    return 0

# 頂点sから頂点tまでの最大フローの総流量を返す（頂点数N、辺のリストedges）
def maxflow(N, s, t, edges):
    # 初期状態の残余プログラム
    G = [list() for _ in range(N+1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))
    INF = 10**10
    total_flow = 0
    while True:
        used = [False]*(N+1)
        F = dfs(s, t, INF, G, used)
        if F>0:
            total_flow += F
        else:
            break  # フローを流せなくなったら、操作終了
    return total_flow
# 入力
N, M = map(int, input().split())
P = list(map(int, input().split()))
A = [0]*M
B = [0]*M
for i in range(M):
    a, b = map(int, input().split())
    A[i], B[i] = a-1, b-1
# グラフを作る（前半パート）
Offset = 0
edges = list()
for i in range(N):
    if P[i]>=0:
        edges.append([N, i, P[i]])
        Offset += P[i]
    if P[i]<0:
        edges.append([i, N+1, -P[i]])

for i in range(M):
    edges.append([A[i], B[i], 10000000000000])
answer = Offset - maxflow(N+2, N, N+1, edges)
print(answer)