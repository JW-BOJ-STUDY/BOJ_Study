import sys

timeItem = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]

sortedItem = sorted(timeItem, key=lambda x : x[1])

start = []
finish = []

for i in range(len(sortedItem)):
    start.append(sortedItem[i][0])
    finish.append(sortedItem[i][1])
    

classNum = 0

while True:
    finish.pop()
    startTime = start.pop()
    N = len(finish)
    while True:
        if startTime in finish:
            a = finish.index(startTime)
            finish.pop(a)
            startTime = start.pop(a)
        else:
            startTime -= 1
            if startTime == 0:
                break
        
    classNum += 1
    if(len(finish) == 0):
        break

sys.stdout.write(str(classNum))