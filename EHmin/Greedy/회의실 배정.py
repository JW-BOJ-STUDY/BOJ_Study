from datetime import time
import sys

timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]

sortedTimeTable = sorted(timeTable, key = lambda x : (x[1], x)) # 최대한 많이 배정하기 위해서는 끝나는 시간이 중요하다.
# 빨리 끝나야 다음 배정이 가능하기 때문이다. 이때 두번째 조건 까지 사용하지 않는다면 같은 시간에 시작하고, 끝나는 문제에서 순서에 따라 오류가 발생 할 수 있다. 
#파이썬에서 사용하는 람다 식 새로운 함수를 만들지 않고, 간단하게 들어오는 x에 대해서 수행할 것을 지정해 줄 수 있다. 

endTime = -1 # 수업이 끝나는 시간
output = 0 # 출력

for item in sortedTimeTable: 
    if item[0] < endTime: # 이미 배정된 강의가 끝나기 전에 시작하는 강의는 무시
        continue
    else : #만약 이전 강의 이후에 시작한다면
        output += 1 # 가능한 강의의 수를 하나 늘리고, 
        endTime = item[1] # 새로운 강의의 끝나는 시간을 저장한다. 
        
sys.stdout.write(str(output))
