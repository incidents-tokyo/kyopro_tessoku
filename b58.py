import bisect
# seg[pos] = x
def update(pos, x):
    pos += siz
    dat[pos] = x
    while pos>=2:
        pos //= 2
        dat[pos] = min(dat[pos*2], dat[pos*2+1])
# min(seg[l], seg[l + 1], ..., seg[r - 1])
def query(l, r):
    l += siz
    r += siz
    answer = INF
    while l < r:
        if l >= 1:
            if answer > dat[l]:
                answer = dat[l]
            l += 1
        if r >= 1:
            r -= 1
            if answer > dat[r]:
                answer = dat[r]
        l //= 2
        r //= 2
    return answer

INF = 1 << 61
N, L, R = map(int, input().split())
X = list(map(int, input().split()))
# dp[i]: i番の足場までのジャンプの最小回数
dp = [0]*N
siz = 1
while N>=siz:
    siz *= 2
# dat[pos+siz-1]: pos番のジャンプの最小回数
dat = [INF]*siz*2
update(0, dp[0])
for i in range(1, N):
    # posLとposR: ジャンプ可能なひとつ前の足場の端pos X[i]-R<=X[pos]<=X[i]-L ~ X[i]
    posL = bisect.bisect_left(X, X[i]-R)
    posR = bisect.bisect_right(X, X[i]-L)
    # dp[posL]からdp[posR]までの最小値を求める
    dp[i] = query(posL, posR) + 1
    update(i, dp[i])
print(dp[-1])