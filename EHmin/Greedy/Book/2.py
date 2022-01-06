import sys

column, row = map(int, sys.stdin.readline().split())

cards = [list(map(int, sys.stdin.readline().split())) for _ in range(column)]

output = 0

for i in range(column):
    cards[i].sort()
    if cards[i][0] >= output: output = cards[i][0]
    
sys.stdout.writelines(str(output))
    
# min(list)를 이용해서 sort 하지 않고 값을 찾을 수 도 있다. 훨씬 빠를듯. 