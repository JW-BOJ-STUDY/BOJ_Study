import sys

N,M = list(map(int,sys.stdin.readline().split()))
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def maxInPoint(i,j): # 모든 포인트에서 계산.
    temp = []
    ### 정사각형 ###
    if i+1 < N and j+1 < M:
        temp.append(paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1] )
    ### 막대기 ###
    if i+3 < N : # 가로
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])
    if j+3 < M : # 세로 
        temp.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]) 
    ### 엿 ###
    if i-1 >= 0 and i+1 < N and j-1 >=0 : # 위 
        temp.append(paper[i-1][j] + paper[i][j] + paper[i+1][j] + paper[i][j-1]) 
    if i-1 >= 0 and i+1 < N and j+1 < M : # 아래 
        temp.append(paper[i-1][j] + paper[i][j] + paper[i+1][j] + paper[i][j+1]) 
    if i+1 < N and j-1 >=0 and j+1 < M: # 오른쪽
        temp.append(paper[i][j-1] + paper[i][j] + paper[i][j+1] + paper[i+1][j]) 
    if i - 1 >= 0 and j-1 >=0 and j+1 < M: # 오른쪽
        temp.append(paper[i][j-1] + paper[i][j] + paper[i][j+1] + paper[i-1][j])      
    ### 번개 ###
    if i+2 < N and j-1 >=0 :                                                           
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j-1])  
    if i+2 < N and j+1 <M :                                                           
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1])   
    if i+1 < N and j+2 <M :                                                           
        temp.append(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2])  
    if i-1 >= 0 and j+2 <M :
        temp.append(paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-1][j+2]) 
    if i-2 >= 0 and j+1 <M :
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-1][j+1] + paper[i-2][j+1])
    if i-2 >= 0 and j-1 >=0 :
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-1][j-1] + paper[i-2][j-1])
    if i-1 >= 0 and j-2 >=0 :
        temp.append(paper[i][j] + paper[i][j-1] + paper[i-1][j-1] + paper[i-1][j-2])
    if i+1 < N and j-2 >=0 :
        temp.append(paper[i][j] + paper[i][j-1] + paper[i+1][j-1] + paper[i+1][j-2]) 
    ### ㄱ ###
    if i+2 < N and j+1 < M:##
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]) 
    if i+1 < N and j+2 < M:
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2])      
    if i+2 < N and j+1 < M:
        temp.append(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1])
    if i+1 < N and j+2 < M:
        temp.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2])##
    if i-2 >= 0 and j+1 < M:##
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-2][j] + paper[i-2][j+1]) 
    if i-1 >= 0 and j+2 < M:
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-1][j+1] + paper[i-1][j+2])      
    if i-2 >= 0 and j+1 < M:
        temp.append(paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-2][j+1])
    if i-1 >= 0 and j+2 < M:
        temp.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+2])##
    if i-2 >= 0 and j-1 >= 0:##
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-2][j] + paper[i-2][j-1]) 
    if i-1 >= 0 and j-2 >= 0:
        temp.append(paper[i][j] + paper[i-1][j] + paper[i-1][j-1] + paper[i-1][j-2])      
    if i-2 >= 0 and j-1 >= 0:
        temp.append(paper[i][j] + paper[i][j-1] + paper[i-1][j-1] + paper[i-2][j-1])
    if i-1 >= 0 and j-2 >= 0:
        temp.append(paper[i][j] + paper[i][j-1] + paper[i][j-2] + paper[i-1][j-2])##
    if i+2 < N and j-1 >= 0:##
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j-1]) 
    if i+1 < N and j-2 >= 0:
        temp.append(paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+1][j-2])      
    if i+2 < N and j-1 >= 0:
        temp.append(paper[i][j] + paper[i][j-1] + paper[i+1][j-1] + paper[i+2][j-1])
    if i+1 < N and j-2 >= 0:
        temp.append(paper[i][j] + paper[i][j-1] + paper[i][j-2] + paper[i+1][j-2])##
    return max(temp)
           
output = []

for i in range(M*N):
    output.append(maxInPoint(i//M, i%M))
    
print(max(output))