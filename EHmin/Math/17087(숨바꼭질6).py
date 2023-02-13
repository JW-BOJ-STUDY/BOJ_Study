from sys import stdin
import math
input = stdin.readline

N,S = map(int, input().split())
location_abs = list(map(int,input().split()))
location_abs.append(S)

location_start = min(location_abs) # 어차피 상대 위치이므로 시작점을 바꿔도 무관
location_rel = []

for loc in location_abs:
    location_rel.append(loc - location_start)

print(math.gcd(*location_rel)) # 파이썬에서 *는 언패킹 오퍼레이터!