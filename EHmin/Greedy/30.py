import sys

Number = list(map(int, sys.stdin.readline().strip()))

Number.sort(reverse = True)

if (sum(Number) % 3 == 0) and min(Number) == 0:
    sys.stdout.write("".join(map(str, Number)))
else:
    sys.stdout.write("-1")
    