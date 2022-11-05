N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
grundy = [0]*(10**5+1)
for i in range(10**5+1):
    trans = {0:False, 1:False, 2:False}
    if i-X>=0:
        trans[grundy[i-X]] = True
    if i-Y>=0:
        trans[grundy[i-Y]] = True
    keys = [k for k, v in trans.items() if v == False]
    grundy[i] = min(keys)
ans = 0
for a in A:
    ans ^= grundy[a]
print('First' if ans!=0 else 'Second')

'''
Grundy数: 盤面の状態に番号がついている
Grundy数が0の状態は, 必勝状態
Grundy数が意味することは, その値未満の任意の非負整数の状態に遷移できる
'''

'''
速いコード
  for i in range(100001):
    trans = [True, True, True]
    if i >= x: trans[grundy[i-x]] = False
    if i >= y: trans[grundy[i-y]] = False
    if trans[0]: grundy[i] = 0
    elif trans[1]: grundy[i] = 1
    else: grundy[i] = 2
'''
