# 参考
import copy
# 1回目の操作（P[i], Q[i], R[i]）を表す構造体
class round:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

# 盤面の状態を表す構造体
class state:
    # 盤面の状態の初期化
    def __init__(self, n):
        self.score = 0  # 暫定スコア
        self.x = [0]*n  # 現在の配列xの値
        self.lastmove = '?'  # 最後の動き（'A'または'B'、ただし初期状態では'?'としておく）
        self.lastpos = -1  # Beam[i-1][どこ]から遷移したか（ただし初期状態では-1としておく）

# ビームサーチを行う関数
def beam_search(N, T, rounds):
    # 2次元配列beamを用意し、0手目の状態を設定
    WIDTH = 350
    beam = [list() for i in range(T+1)]
    beam[0].append(state(N))

    # ビームサーチ
    for i in range(T):
        candidate = list()
        for j in range(len(beam[i])):
            # 操作Aの場合
            op_a = copy.deepcopy(beam[i][j])
            op_a.lastmove = 'A'
            op_a.lastpos = j
            op_a.x[rounds[i].p] += 1
            op_a.x[rounds[i].q] += 1
            op_a.x[rounds[i].r] += 1
            op_a.score += op_a.x.count(0)  # スコアに「op_a.xに含まれる0の個数」を加算
            # 操作Bの場合
            op_b = copy.deepcopy(beam[i][j])
            op_b.lastmove = 'B'
            op_b.lastpos = j
            op_b.x[rounds[i].p] -= 1
            op_b.x[rounds[i].q] -= 1
            op_b.x[rounds[i].r] -= 1
            op_b.score += op_b.x.count(0)  # スコアに「op_b.xに含まれる0の個数」を加算
            # 候補に追加
            candidate.append(op_a)
            candidate.append(op_b)
        # ソートしてbeam[i+1]の結果を計算する
        candidate.sort(key = lambda s: -s.score)
        beam[i+1] = copy.deepcopy(candidate[:WIDTH])  # 多くともcandidateの上位WIDTH件しか記録しない
    
    # ビームサーチの復元
    current_place = 0
    answer = [None]*T
    for i in range(T, 0, -1):  # T,T-1,~,1
        answer[i-1] = beam[i][current_place].lastmove
        current_place = beam[i][current_place].lastpos
    return answer

# 入力
T = int(input())
rounds = [None]*T
for i in range(T):
    p, q, r = map(int, input().split())
    rounds[i] = round(p-1, q-1, r-1)  # 0-indexed
    
# ビームサーチを行って答えを出す
answer = beam_search(20, T, rounds)

# 出力
for c in answer:
    print(c)