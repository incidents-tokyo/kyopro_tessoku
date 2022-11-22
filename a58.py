def update(pos, x):
    pos = pos + siz - 1
    dat[pos] = x
    while pos>=2:
        pos //= 2
        dat[pos] = max(dat[pos*2], dat[pos*2+1])
# l~r区間の最大値を求める, uは現在のセル番号, [a, b)はセルに対応する半開区間
def query(l, r, a, b, u):
    if r<=a or b<=l:
        return -1000000000
    if l<=a and b<=r:
        return dat[u]
    m = (a+b)//2
    AnswerL = query(l, r, a, m, u*2)
    AnswerR = query(l, r, m, b, u*2+1)
    return max(AnswerL, AnswerR)
N, Q = map(int, input().split())
siz = 1
while N>siz:
    siz *= 2
dat = [0]*siz*2
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0]==1:
        pos, x = q[1], q[2]
        update(pos, x)
    if q[0]==2:
        l, r = q[1], q[2]
        print(query(l, r, 1, siz+1, 1))