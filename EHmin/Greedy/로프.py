import sys

lope = [int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))]

sotredLope = sorted(lope)

output = 0 

for i in range(len(lope)):
    if output <= sotredLope[len(lope) - i - 1] * (i+1) : 
        output = sotredLope[len(lope) - i - 1] * (i+1)
    else : continue
    
print(output)