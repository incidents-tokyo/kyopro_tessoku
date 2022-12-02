def update(pos, x):
    pos = pos + siz - 1
    dat[pos] = x
    while pos>=2:
        pos //= 2
        dat[pos] = dat[pos*2]+dat[pos*2+1]

# uは現在のセル番号、[a,b)はセルに対応する半開区間、[l,r)は求めたい半開区間
def query(l, r, a, b, u):
    if r<=a or b<=l:
        return 0
    if l<=a and b<=r:
        return dat[u]
    m = (a+b)//2
    AnswerL = query(l, r, a, m, u*2)
    AnswerR = query(l, r, m, b, u*2+1)
    return AnswerL+AnswerR

N = int(input())
A = list(map(int, input().split()))
siz = 1
max_A = 150000+1
while max_A>siz:
    siz *= 2
# dat[x]: 現時点で整数xは何回出現したか
dat = [0]*siz*2
ans = 0
for x in A:
    ans += query(x+1, max_A, 1, siz+1, 1)
    update(x, dat[x+siz-1]+1)
print(ans)