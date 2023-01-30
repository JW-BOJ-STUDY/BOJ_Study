n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))


# 이건... 너무 수학의 성질가지고 문제푸는거 같은데.. 이런문제도 나오려나..