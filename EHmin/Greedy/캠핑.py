from asyncore import read
import sys

output = []

while True: #계속해서 케이스를 입력받다, 만약 0이 들어오면 종료
    dayList = list(map(int, sys.stdin.readline().split()))
    if dayList[0] == 0:
        break
    # 가장빠른 시점부터 채워야 최대로 가능
    # 최대 반복횠수를  repetition에 저장.
    repetition = dayList[2] // dayList[1] 
    # remainder에 반복하고 난 나머지를 계산. 
    remainder = dayList[2] % dayList[1]
    if remainder >= dayList[0]: # 만약 나머지가 연속한 날중에 가능한 날 수(dayList[0) 보다 크면 dayList[0]만 더해줌
        output.append((repetition + 1) * dayList[0])
    else:# 반대로 remainder가 dayList[0]다 작으면 모두 더 들어가도 된다. 
        output.append(repetition * dayList[0] + remainder)

for i in range(len(output)):
    sys.stdout.write("Case " + str(i + 1) + ": " + str(output[i]) +"\n")