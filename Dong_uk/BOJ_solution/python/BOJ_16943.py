import itertools #순열 찾아주는 라이브러리

A,B = input().split()

AA = [] 
##A = list(A)
A = itertools.permutations(A,len(A))
for i in A:
    AA.append(''.join(i))

##A.sort(reverse=True)
minBig = -1 #다른 코드없이 바로 -1로 해둔다

for i in AA:
    if i[0] == '0':  # 0으로 시작하는 경우
        continue
    elif int(i) < int(B):
        minBig = max(int(i),minBig)
print(minBig)