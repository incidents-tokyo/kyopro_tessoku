print(int(input(), 2))
'''
他の人の解答
N = input()
ans = 0
for i in range(1,len(N)+1):
    a = int(N[-i])*(2**(i-1))
    ans += a
print(ans)
'''