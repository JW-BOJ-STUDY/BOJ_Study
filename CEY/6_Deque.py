# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

num = (int)(input())
d_list = [input().split() for _ in range(num)]
mydeque = []

for i in range(num):
    if d_list[i][0] == "push_front" :
        mydeque.insert(0,d_list[i][1])
    
    elif d_list[i][0] == "push_back" :
        mydeque.append(d_list[i][1])
    
    elif d_list[i][0] == "pop_front" :
        if len(mydeque) == 0:
            print(-1)
        else: 
            print(mydeque.pop(0)) 
    
    elif d_list[i][0] == "pop_back" :
        if len(mydeque) == 0:
            print(-1)
        else: 
            print(mydeque.pop(-1)) 
    
    elif d_list[i][0] == "size" :
        print(len(mydeque))

    elif d_list[i][0] == "empty" :
        if len(mydeque) == 0:
            print(1)
        else:
            print(0)
    
    elif d_list[i][0] == "front" :
        if len(mydeque) == 0:
            print(-1)
        else: 
            print(mydeque[0])

    elif d_list[i][0] == "back" :
        if len(mydeque) == 0:
            print(-1)
        else: 
            print(mydeque[-1])