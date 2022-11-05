N, A, B = map(int, input().split())
state = [False]*(N+1)
for i in range(N+1):
    if i-A>=0 and not state[i-A]:
        state[i] = True
    elif i-B>=0 and not state[i-B]:
        state[i] = True
print('First' if state[N] else 'Second')