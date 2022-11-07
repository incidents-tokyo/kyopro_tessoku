import heapq
T = []
Q = int(input())
for _ in range(Q):
    query = input()
    num = query[0]
    if num=='1':
        heapq.heappush(T, int(query[2:]))
    elif num=='2':
        ans = heapq.heappop(T)
        print(ans)
        heapq.heappush(T, ans)
    else:
        heapq.heappop(T)