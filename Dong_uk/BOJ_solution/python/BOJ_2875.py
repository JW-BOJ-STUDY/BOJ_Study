#남자 여자 비율이 1:2
F, M, K = map(int,input().split())

result = 0
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
