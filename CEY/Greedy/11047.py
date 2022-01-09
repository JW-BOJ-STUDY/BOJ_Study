# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys


def input():
    return sys.stdin.readline().rstrip()


num, money = map(int, input().split())
count = 0

coin_list = []

for i in range(num):
    coin = int(input())
    coin_list.append(coin)

while money != 0:
    ncoin = coin_list.pop()
    count += money // ncoin
    money %= ncoin

print(count)
