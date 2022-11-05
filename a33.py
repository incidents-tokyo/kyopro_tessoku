N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans ^= a
print('First' if ans != 0 else 'Second')
'''
    「ニム和が0以外」 -(遷移)-> 「ニム和が0」となる手が存在
    「ニム和が0」 -(遷移)-> 絶対に「ニム和が0以外」
    (勝つときの石の状態は「ニム和が0以外」のとき)
'''