import sys 
'''
## 시간초과 이슈 때문에 다른 방식 필요
##N = list(int(sys.stdin.readline().split()))
N,M = map(int,input().split())

countB = 0 

for i in range(N,M+1):
    
    countS = 0
    i = str(i)

    for ii in i:
        if ii == '4' or ii=='7':
            countS += 1
            continue
        else :
            countS = 0 #아닐경우 초기화 필요
            break
    countB += countS / len(i)

print(int(countB))
'''

def dfs(lower,upper,depth,number):
    answar = 0 
    if depth >= 10:
        return 0
    if number > upper:
        return 0 #위로 범위  벗어날시 노카운트
    if upper >= number >= lower :
        answar+=1
    answar += dfs(lower,upper,depth+1,number*10+4)
    answar += dfs(lower,upper,depth+1,number*10+7)
    return answar

A,B = map(int,input().split())
ans = dfs(A,B,0,0)
print(ans)