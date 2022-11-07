from collections import deque
Q = int(input())
S = deque()
for _ in range(Q):
    query = input()
    num = query[0]
    if num=='1':
        S.append(query[2:])
    elif num=='2':
        print(S[-1])
    elif num=='3':
        S.pop()