import sys

N = int(sys.stdin.readline().strip())
time = list(map(int , sys.stdin.readline().split())) #list 로 한번 감싸줘야함

STime = sorted(time)

waitTime = 0
output = 0 

for item in STime:
    waitTime += item
    output += waitTime
    
print(output)