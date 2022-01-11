
a,b = input().split()

a = int (a)
b = int (b)

arr = []
arr = list(range(1,a+1))

loc = input().split()
loc =list(map(int,loc))

count = 0

while True:
    
    if arr[0] == loc[0] : 
        del arr[0]
        del loc[0]
        
    elif loc[0]<=len(arr)/2:
        alpa = arr.pop(0)
        arr.append(alpa)
        count += 1
        
    elif loc[0] > len(arr)/2:
        alpa = arr.pop()
        arr.insert(0,alpa)
        count += 1
        
    if len(loc)==0:
        break

print (count)
