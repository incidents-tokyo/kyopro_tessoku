N = int(input())
A = [[i, list(map(int, input().split()))] for i in range(N)]
Q = int(input())
for _ in range(Q):
    Type, x, y = map(int, input().split())
    if Type==1:
        i = 0
        while A[i][0]!=x-1:
            i += 1
        j = 0
        while A[j][0]!=y-1:
            j += 1
        A[i][0], A[j][0] = A[j][0], A[i][0]
    if Type==2:
        i = 0
        while A[i][0]!=x-1:
            i += 1
        print(A[i][1][y-1])
'''
参考
import sys
import pypyjit
import itertools
import heapq
import math
from collections import deque, defaultdict
import string
import functools
import bisect

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
pypyjit.set_param('max_unroll_recursion=-1')


def readints(): return map(int, input().split())
def readlist(): return list(map(int, input().split()))
def readstr(): return input()[:-1]


N = int(input())
A = [readlist() for _ in range(N)]

row = [i for i in range(N)]
Q = int(input())
for _ in range(Q):
    t, x, y = readints()
    x -= 1
    y -= 1
    if t == 1:
        row[x], row[y] = row[y], row[x]
    else:
        print(A[row[x]][y])

'''