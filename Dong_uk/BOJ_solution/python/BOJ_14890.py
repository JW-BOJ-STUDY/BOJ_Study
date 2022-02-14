N,L=map(int,input().split())

map = [list(map(int,input().split())) for _ in range(N)]    #이렇게 바로 만들기도 하는거 확인

ans = 0
for i in range(N):
    a = map[i][0]
    cnt = 1 #1하나 먹고 시작
    for ii in range(1,N): #맨앞은 필요없음
        if map[i][ii] == a:
            a = map[i][ii]
            cnt +=1
        elif map[i][ii] == a+1 and cnt >= 0:
            if cnt >= L:
                cnt = 1#초기화
                a = map[i][ii]
            else :
                break
        elif map[i][ii] == a-1 and cnt >= 0:
            cnt = -L+1 #오르락 내리락 방지
            a = map[i][ii]
        else :
            break
    else: #for-else 문 for문이 끝까지 수행된 경우 실행된다
        if cnt >= 0:
            ans += 1 #남는 내리막이 없어야지만 끝까지 확인

for ii in range(N):
    a = map[0][ii]
    cnt = 1 #1하나 먹고 시작
    for i in range(1,N): #맨앞은 필요없음
        if map[i][ii] == a:
            a = map[i][ii]
            cnt +=1
        elif map[i][ii] == a+1 and cnt >= 0:
            if cnt >= L:
                cnt = 1#초기화
                a = map[i][ii]
            else :
                break
        elif map[i][ii] == a-1 and cnt >= 0:
            cnt = -L+1 #오르락 내리락 방지
            a = map[i][ii]
        else :
            break
    else: #for-else 문 for문이 끝까지 수행된 경우 실행된다
        if cnt >= 0:
            ans += 1 #남는 내리막이 없어야지만 끝까지 확인

print(ans)