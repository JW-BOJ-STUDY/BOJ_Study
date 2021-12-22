N , K = input().split()
n = int(N)
k = int(K)
index = k - 1 

list = [i for i in range(n)]

outputList = []

while True:
    outputList.append(str(list.pop(index) + 1))
    if len(list) == 0:
        break
    index += k - 1
    index = (index % len(list))
             
print("<"+ ", ".join(outputList) + ">")