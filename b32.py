N, K = map(int, input().split())
A = list(map(int, input().split()))
state = [False]*(N+1)
for i in range(N+1):
    for a in A:
        if i-a>=0 and not state[i-a]:
            state[i] = True
            break
print('First' if state[N] else 'Second')