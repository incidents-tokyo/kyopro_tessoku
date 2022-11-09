Q = int(input())
S = {}
for _ in range(Q):
    query = input()
    num = query[0]
    if num=='1':
        _, name, score = query.split()
        S[name] = score
    elif num=='2':
        _, name = query.split()
        print(S[name])
'''
よいコード
Q = int(input())
queries = [tuple(input().split()) for _ in range(Q)]

records = {}
for op, name, *score in queries:
    if op == "1":
        records[name] = int(score[0])
    else:
        print(records[name])
# query = [x for x in input().split()]
# num=A[0], name=A[1], score=A[2]
'''
