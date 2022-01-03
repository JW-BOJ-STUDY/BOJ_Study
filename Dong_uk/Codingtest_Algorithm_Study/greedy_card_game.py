N , M = map(int, input().split())

result = 0

for i in range(N): #python 특성상 과감하게 버린 M
    card = list(map(int, input().split()))
    line_min = min(card)
    result = max(line_min, result)

print(result)