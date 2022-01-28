N = int(input())
list1 = list(map(int,input().split()))
B,C = map(int,input().split())

count = 0

for i in list1 : 
    if (i - B) > 0:
        count+=1
        count += (i-B)//C
        if(i-B)%C > 0:
            count+=1 
    else:
        count+=1     

print(count)
