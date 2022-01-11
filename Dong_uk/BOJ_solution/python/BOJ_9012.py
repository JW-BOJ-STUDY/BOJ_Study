num =  int(input())
for i in range(num):
    a = input()
    Stack = []
    a = list(a)
    
    for j in a:
        if j == '(':
            Stack.append(j)    
        elif j == ')':
            if len(Stack) != 0 and Stack[-1] =="(":
                Stack.pop()
            else:
                Stack.append(")")  #ㄹㅇ 어이 털리는부분 이거있음 사실 논리적 말이안됨
                break
                
    if len(Stack) == 0 :
        print('YES')
    else :
        print('NO')
