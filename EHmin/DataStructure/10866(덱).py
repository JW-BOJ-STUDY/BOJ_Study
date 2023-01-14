from sys import stdin, stdout

input = stdin.readline
print = stdout.write

my_queue = []

for _ in range(int(input())):
    order = input().split()
    
    if order[0] == "push_front":
        my_queue.insert(0,order[1])
    
    elif order[0] == "push_back":
        my_queue.append(order[1])
        
    elif order[0] == "pop_front":
        if len(my_queue) == 0:
            print("-1\n")
        else:
            print(my_queue.pop(0) + "\n")
            
    elif order[0] == "pop_back":
        if len(my_queue) == 0:
            print("-1\n")
        else:
            print(my_queue.pop() + "\n")
            
    elif order[0] == "size":
        print(str(len(my_queue))+"\n")
        
    elif order[0] == "empty":
        if len(my_queue) == 0:
            print("1\n")
        else:
            print("0\n")
            
    elif order[0] == "front":
        if len(my_queue) == 0:
            print("-1\n")
        else:
            print(my_queue[0] + "\n")
    else:
        if len(my_queue) == 0:
            print("-1\n")
        else:
            print(my_queue[-1] + "\n")
            