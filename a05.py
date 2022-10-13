N, K = map(int, input().split())
answer = 0
for x in range(1,N+1):
    for y in range(1,N+1):
        z = K-x-y
        if 1<=z<=N:
            answer += 1
print(answer)