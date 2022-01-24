i=0
while True:
    i += 1
    L,P,V = map(int,input().split())
    if L+P+V == 0:
        break
    a = V//P
    b = V%P
    if L<b:
        b = L
    print("Case %d: %d" %(i, a*L+b))