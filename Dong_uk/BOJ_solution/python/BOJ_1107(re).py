#양심적으로 500000까지
#brute force를 사용해야한다는것을 유추

N = int(input())
M = int(input())

temp = 100
bestCount = abs(100-N)

notBroken = {'0','1','2','3','4','5','6','7','8','9'} ##연산이 불가하다는 list를 극복하기 위해 set사용 
## str형으로 안해서 오류 미쳣었음 형일치 주의

if M != 0 :
    notBroken -= set(map(str, input().split()))

for i in range(1000000): ##내려오는 경우도 생각하여야한다
    for ii in str(i): ## 당연히 i인데 N으로 헷갈렸다
        if ii not in notBroken:
            break

        elif len(str(i))+abs((N-i)) < bestCount:
            bestCount = len(str(i))+abs((N-i))
    '''
    else :
        bestCount = min(bestCount, len(str(i)) + abs(i - N))
    '''
print (bestCount)