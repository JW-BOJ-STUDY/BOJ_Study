# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거술러 줘야할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

import sys


def input():
    return sys.stdin.readline().rstrip()


# < 내 방법 >
money = int(input())
count = 0

count += money//500
money = money % 500

count += money//100
money = money % 100

count += money//50
money = money % 50

count += money//10
money = money % 10

# < 책 방법 >
money = int(input())
count = 0

mlist = [500, 100, 50, 10]
for i in mlist:
    count += money // i
    money %= i

print(count)
