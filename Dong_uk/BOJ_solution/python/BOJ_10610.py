Num = list(input())
Num.sort(reverse=True)
sum = 0

for i in Num :
    Num += int(i)

if sum % 3 != 0 or "0" not in Num :
    print(-1) 
else: 
    print(''.join)
