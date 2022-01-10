food_times = [1,1,1,1,1,1]
k=30

def solution(food_times,k):
    a=0
    for i in range(0,len(food_times)) :    
        print(1)
        if k ==0 and food_times[i] > 0:
            ##정답이 되려면 k가 0이고 시간이 0이 아니여야한다
            print(2)
            answer = i+1
            return answer
            break     
        
        elif food_times[i] > 0 :
            print(3)
            food_times[i] = food_times[i]-1     
            k = k-1
        elif sum(food_times)==0:
            print(4)
            answer = -1
            return answer
            break
        
        a= a+1
        print(food_times)

        if a == len(food_times):
            print(food_times)
            return solution(food_times,k)
            break



print (solution(food_times,k))
