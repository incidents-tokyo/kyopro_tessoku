from collections import deque
Q = int(input())
T = deque()
for _ in range(Q):
    query = input()
    num = query[0]
    if num=='1':
        T.append(query[2:])
    elif num=='2':
        print(T[0])
    else:
        T.popleft()