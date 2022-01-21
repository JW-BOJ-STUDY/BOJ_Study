#남자 여자 비율이 1:2
F, M, K = map(int,input().split())

'''
while K > 0 :
    MM = 2*M      
    if F > MM : 
        K = K - (F - MM)
        F = MM
    elif F < MM :
        K = K - ((MM - F)//2)
        M = M - ((MM - F)//2)
    elif F == MM : 
        F -= 2
        M -= 1
        K -= 3 
print (min(F//2, M))
'''

result = 0
while F >= 2 and M >= 1 and F+M >= K+3:
    F -= 2
    M -= 1
    result += 1
print(result)
