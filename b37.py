# 参考
N = int(input())
Power10 = [1]*17
for i in range(1, 17):
    Power10[i] = 10*Power10[i-1]
# R[i][j]: 下からi桁目の数字がjとなる、0以上N以下の整数は何個か？
R = [[0]*10 for _ in range(18)]
for i in range(15):
    Digit = (N//Power10[i])%10
    for j in range(10):
        if j < Digit:
            R[i][j] = (N//Power10[i+1])*Power10[i] + Power10[i]
        if j == Digit:
            R[i][j] = (N//Power10[i+1])*Power10[i] + (N%Power10[i]) + 1
        if j > Digit:
            R[i][j] = (N//Power10[i+1])*Power10[i]
ans = 0
for i in range(16):
    for j in range(10):
        ans += j * R[i][j]
print(ans)