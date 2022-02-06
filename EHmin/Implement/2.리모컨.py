import sys

N = int(sys.stdin.readline().strip())
sys.stdin.readline().strip()
brokenNumber = list(map(int,sys.stdin.readline().split()))

def NumCheck(x): # x가 내가 누를수 있는 버튼으로만 이루어진 숫자인지 확인해주는 함수
    for num in brokenNumber:
        if str(x).find(str(num)) != -1:
            return False
    return True

## 전체적인 아이디어: 일단 내가 도달하고자 하는 수에서 부터 한칸씩 양쪽으로 이동. 
## 이동하다가 내가 만들 수 있는 수 만나면 멈춤

onlyPlusMinus = abs(N - 100) #플마 버튼만 눌러서 도착하는 경우 

goUp = N #원하는 수 부터 위로 올라감
goDown = N # 원하는 수 부터 아래로 내려감
downFrom100 = 100 # 100부터 아래로 이동
upFrom100 = 100 # 100 부터 위로 이동
count = 0

up = True #움직이는 방향에 따라 자리수가 변하면 누르는 버튼의 수가 바뀔 수 있음. 
# 따라서 위로 가는지 아래로 가는지 체크해줌

while True:
    if NumCheck(goDown):
        up = False
        break
    elif NumCheck(goUp):
        up = True
        break
    elif downFrom100 == N or upFrom100 == N: # 버튼이 모두 망가지는경우 while을 빠져나가기 위한 조건
        break
    goUp += 1
    goDown -= 1
    if goDown < 0: goDown = 0 #0보다 작아질 수 없음. 제발 조건 무시하지 말고 구현하자. 
    downFrom100 -= 1
    upFrom100 += 1
    count += 1 #한칸씩 이동
    
closeNum = 0 # 내가 누를 수 있는 수중 가장 가까운 수

if up:
    closeNum = goUp
else :
    closeNum = goDown
     
if onlyPlusMinus >= count + len(str(closeNum)):
    print(count + len(str(closeNum)))
else:
    print(onlyPlusMinus)
    
    