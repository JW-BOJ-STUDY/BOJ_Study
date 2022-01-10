N,M = map(int,input().split())

if N == 1 :
    print(1)
elif N == 2 :
    print(min(4,(M-1) // 2 +1 ))
elif N >= 3 :
    if M < 7:
        print(min(M,4))
    elif M >= 7 :
        print(M - 2)
