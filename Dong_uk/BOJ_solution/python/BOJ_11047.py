N,K = map(int, input().split())

coin = []
lostArk = 0

for i in range(N):
    coin_temp = int(input())
    coin.append(coin_temp)


while K != 0:
    lostArk += K // coin[-1]
    K = K % coin[-1]
    coin.pop(-1)
print(lostArk)