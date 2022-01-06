# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

import sys


def input():
    return sys.stdin.readline().rstrip()


N, M, K = map(int, input().split())
numarr = list(map(int, input().split()))
snumarr = sorted(numarr)
maxnum = 0

if K <= M:
    maxnum = (M//(K+1))*(snumarr[-1]*K+snumarr[-2])+(M % (K+1))*snumarr[-1]

print(maxnum)
