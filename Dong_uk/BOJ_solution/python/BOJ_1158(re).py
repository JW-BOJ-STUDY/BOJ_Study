# person_total,person_out = input().split()
# person_total = int(person_total)
# person_out = int(person_out)

person_total,person_out= map(int,input().split())

pivot = 0 
outputQ = []

#for i in range(person_total):
#    compareList.append(i+1)
compareList = [i+1 for i in range(person_total)]

for i in range(person_total):
    pivot =pivot + person_out-1  
    if pivot>= len(compareList):   
        pivot = pivot%len(compareList) # - 가 아닌 % 사용해야함
 
    outputQ.append(str(compareList.pop(pivot)))
        
# lenQ = len(outputQ)
# print("<",end = "")
# for i in range(lenQ):
#     if i+1 == lenQ:
#         print(outputQ.pop(0), end = '')
#     elif i < lenQ:
#         print(outputQ.pop(0), end = ', ')
# print(">",end = "")

print("<",", ".join(outputQ)[:],">", sep='')