# BOJ1005
# ACM Craft

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))

    before_build = {x : [] for x in range(1, N+1)}

    for _ in range(K):
        x, y = map(int, input().split())
        before_build[y].append(x)

    W = int(input())
