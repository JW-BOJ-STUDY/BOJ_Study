import sys

start, end = sys.stdin.readline().split()

# 각각 이전까지 금민수의 개수를 찾아서 빼주겠다. 

def numberOfGMNumberBelow(arr, smaller):
    
    def equalNum2GMNumber(arr): # 해당 자리수에서, arr번째 금민수를 리턴해준다. ex) 000 > 444, 010 > 474
        output = []
        for number in arr:
            if int(number) == 0:
                output.append('4')
            else:
                output.append('7')
        return int("".join(output))
 
    underNum = 0 # 해당 자리수 이전의 모든 금민수의 개수를 계산. 

    for i in range(len(arr)):
        underNum += 2**(i)

    equalNum = 0 # 주어진 수보다 작은 동일 자리수의 금민수의 개수

    f = "0" + str(len(arr)) + "b" # 주어진 자리수 만큼을 이진수로 표현 ex) 000 > 001 > 002 > 003 
    
    while True:
            if equalNum2GMNumber(format(equalNum, f)) < int(arr):
                equalNum += 1
            elif equalNum2GMNumber(format(equalNum, f)) == int(arr):
                if smaller :
                    break
                else:
                    equalNum +=1
            else:
                break
        
    return equalNum + underNum


print( numberOfGMNumberBelow(end, False) - numberOfGMNumberBelow(start, True))


# 77 74 44 45       77 75 