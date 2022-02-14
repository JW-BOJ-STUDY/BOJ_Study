# 시도할 방법 도형 관점 ? 위치 관점 ? 
# 도형관점으로 5개의 도형을 모든 case로 나누어 최고값을 도출하겠다

# 모든 조합을 찾은 후에 sort 그리고 인접성 조사

def shape1_1():
    ans = 0
    for i in range(N):
        for ii in range(M): 
            score  =  0
            if ii+4 > M: #+3? 4? 이 되어야하나?
                break
            for iii in range(ii,ii+4):
                score += scoreBoard[i][iii]
            ans = max(ans,score)
    #print(ans)
    return ans

def shape1_2():
    ans = 0 
    for i in range(M):
        for ii in range(N):   
            score  =  0
            if ii+4 > N:
                break
            for iii in range(ii,ii+4):
                score += scoreBoard[iii][i]
            ans = max(ans,score)
    #print(ans)
    return score

def shape2():
    ans = 0
    for i in range(N):
        if i+2 > N : 
            break
        score = 0
        for ii in range(M):
            if ii+2 >M :
                break
            score = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i+1][ii]+scoreBoard[i+1][ii+1]
            ans = max(score,ans)
    #print(ans)
    return ans

def shape3(): 
    ans = 0 
    for i in range(N):
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        for ii in range(M):
            if i+2 < N and ii+1 < M:
                score1 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+2][ii]+scoreBoard[i+2][ii+1]
            if i+2 < N and ii > 0: # or ii-1 > 0
              score2 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+2][ii]+scoreBoard[i+2][ii-1]
            if i+1 < N and ii+2 < M: 
              score3 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i][ii+2]+scoreBoard[i+1][ii+2]
            if i > 0 and ii+2 < M:
                score4 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i][ii+2]+scoreBoard[i-1][ii+2]
            if i > 1 and ii+1 < M:
                score5 = scoreBoard[i][ii]+scoreBoard[i-1][ii]+scoreBoard[i-2][ii]+scoreBoard[i-2][ii+1]
            if i > 1 and ii > 0:
                score6 = scoreBoard[i][ii]+scoreBoard[i-1][ii]+scoreBoard[i-2][ii]+scoreBoard[i-2][ii-1]
            if i+1 < N and ii > 1: 
                score7 = scoreBoard[i][ii]+scoreBoard[i][ii-1]+scoreBoard[i][ii-2]+scoreBoard[i+1][ii-2]
            if i < 0 and ii > 1:
                score8 = scoreBoard[i][ii]+scoreBoard[i][ii-1]+scoreBoard[i][ii-2]+scoreBoard[i-1][ii-2]            
            ans = max(ans,score1,score2,score3,score4,score5,score6,score7,score8)
            ## case 찾는거 다 찾을수 있나? 규칙을 정해보자 ex위로 올라가지 말기 이런거 
    return ans

def shape4(): 
    ans = 0 
    for i in range(N):
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        for ii in range(M):
            if i+2 < N and ii+1 < M:
                score1 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+1][ii+1]+scoreBoard[i+2][ii+1]
            if i+2 < N and ii > 0: # or ii-1 > 0
              score2 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+1][ii-1]+scoreBoard[i+2][ii-1]
            if i+1 < N and ii+2 < M: 
              score3 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i+1][ii+1]+scoreBoard[i+1][ii+2]
            if i > 0 and ii+2 < M:
                score4 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i-1][ii+1]+scoreBoard[i-1][ii+2]
            if i > 1 and ii+1 < M:
                score5 = scoreBoard[i][ii]+scoreBoard[i-1][ii]+scoreBoard[i-1][ii+1]+scoreBoard[i-2][ii+1]
            if i > 1 and ii > 0:
                score6 = scoreBoard[i][ii]+scoreBoard[i-1][ii]+scoreBoard[i-1][ii-1]+scoreBoard[i-2][ii-1]
            if i+1 < N and ii > 1: 
                score7 = scoreBoard[i][ii]+scoreBoard[i][ii-1]+scoreBoard[i+1][ii-1]+scoreBoard[i+1][ii-2]
            if i < 0 and ii > 1:
                score8 = scoreBoard[i][ii]+scoreBoard[i][ii-1]+scoreBoard[i-1][ii-1]+scoreBoard[i-1][ii-2]            
            ans = max(ans,score1,score2,score3,score4,score5,score6,score7,score8)
            ## case 찾는거 다 찾을수 있나? 규칙을 정해보자 ex위로 올라가지 말기 이런거 
    return ans


def shape5():
    ans = 0
    for i in range(N):
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0

        for ii in range(M): 
            if i+2 < N and ii+1 < M:
                score1 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+2][ii]+scoreBoard[i+1][ii+1]
            if i+2 < N and ii > 0: # or ii-1 > 0
                score2 = scoreBoard[i][ii]+scoreBoard[i+1][ii]+scoreBoard[i+2][ii]+scoreBoard[i+1][ii-1]
            if i+1 < N and ii+2 < M: 
                score3 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i][ii+2]+scoreBoard[i+1][ii+1]
            if i > 0 and ii+2 < M:
               score4 = scoreBoard[i][ii]+scoreBoard[i][ii+1]+scoreBoard[i][ii+2]+scoreBoard[i-1][ii+1]
            ans = max(ans,score1,score2,score3,score4)
    return ans
    

N,M = map(int,input().split())
scoreBoard = []
ans = 0
for _ in range(N):
    scores = list(map(int,input().split()))
    scoreBoard.append(scores)

         
ans = max(shape1_1(),shape1_2(),shape2(),shape3(),shape4(),shape5()) 

print(ans)
