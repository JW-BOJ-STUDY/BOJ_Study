import sys

N,M = list(map(int,sys.stdin.readline().split()))

square = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)] # N행 M열의 리스트에 저장. [[1,2,3], [4,5,6], [7,8,9]]

maxStride = max(N,M) - 1 # 만들 수 있는 최대 크기의 정사각형의 한변의 길이 저장. 

def maxSquare(stride): # stride는 정사각형 변의 길이. 
    for i in range(N*M):
        if i//M +stride >= N or i%M + stride >= M:
            continue
        if square[i//M][i%M] == square[i//M +stride][i%M] == square[i//M][i%M + stride] == square[i//M + stride][i%M + stride]: # 각 모서리의 숫자가 동일하면 리턴.
            return stride + 1 # 정답에서 원하는 크기는 '크기'라기 보다는 정사각형 안에 있는 원소의 개수 이므로 + 1 해주어야 한다. 
    return maxSquare(stride - 1) # 만약 for 문안에서 해결이 되지 않는다면, 보다 작은 stride를 적용해서 재귀 호출. 

sys.stdout.write(str(pow(maxSquare(maxStride), 2)))
        
