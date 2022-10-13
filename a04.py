N = int(input())
ans = list()
for i in range(10):
    ans.append(str((N//(1<<i))%2)) # 2進数i桁目の値
print("".join(ans[::-1]))

'''
うまい人
n = int(input())
print(format(n,"b").zfill(10))
これが書きたかった
n = int(input()) 
 
res = ""
while n > 0:
    res = ("0" if (n & 1 == 0) else "1") + res
    n >>= 1
 
print(res.zfill(10)) 
'''