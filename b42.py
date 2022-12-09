def solve(front, back):
    sum_cards = 0
    for i in range(N):
        if A[i]*front + B[i]*back>=0:
            sum_cards += A[i]*front+B[i]*back
    return sum_cards
N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())
Ans1 = solve(1, 1)
Ans2 = solve(1, -1)
Ans3 = solve(-1, 1)
Ans4 = solve(-1, -1)
print(max(Ans1, Ans2, Ans3, Ans4))