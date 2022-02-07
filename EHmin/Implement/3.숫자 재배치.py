import sys

A, B = sys.stdin.readline().split()

a = list(A) #a문자열을 리스트로 변환
b = list(B) # ...

a.sort(reverse=True)

output = []

def makeBiggest(index):
    index += 1 
    for i in range(len(a)):
        if int(a[i]) == int(b[index]):
            output.append(a.pop(i))
            makeBiggest(index)
            break
        elif int(a[i]) < int(b[index]):
            output.append(a.pop(i))
            output.extend(a)
            break

makeBiggest(-1)

if len(output) == 0:
    output.append('0')
        

if output[0] == '0' or int("".join(output)) >= int("".join(b)):
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str("".join(output)))
