import sys

# class queue():
    
#     def __init__(self):
#         self.list = []
        
#     def push(self, x):
#         self.list.append(x)
    
#     def pop(self):
#         if len(self.list) == 0:
#             return -1
#         else:
#             return self.list.pop(0)
        
#     def size(self):
#         return len(self.list)
    
#     def empty(self):
#         if len(self.list) == 0:
#             return 1
#         else:
#             return 0
    
#     def front(self):
#         if len(self.list) == 0:
#                 return -1
#         else:
#             x = self.list.pop(0)
#             self.list.insert(0 , x)
#             return x
        
#     def back(self):
#         if len(self.list) == 0:
#             return -1
#         else:
#             x = self.list.pop()
#             self.list.append(x)
#             return x
    

    
N = int(sys.stdin.readline().strip())
myQueue = list()

for i in range(N):
    arr = sys.stdin.readline().split()
    
    if arr[0] == "push":
        myQueue.append(arr[1])
        
    elif arr[0] == "pop":
        if len(myQueue) == 0:
            sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write(myQueue.pop(0) + "\n")
        
    elif arr[0] == "size":
        sys.stdout.write(str(len(myQueue)) + "\n")
        
        
    elif arr[0] == "empty":
        if len(myQueue) == 0:
                sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write("0" + "\n")
        
    elif arr[0] == "front":
        if len(myQueue) == 0:
            sys.stdout.write("-1" + "\n")
        else:
            x = myQueue.pop(0)
            myQueue.insert(0 , x)
            sys.stdout.write(x + "\n")
        
    elif arr[0] == "back":
        if len(myQueue) == 0:
            sys.stdout.write("-1" + "\n")
        else:
            x = myQueue.pop()
            myQueue.append(x)
            sys.stdout.write(x + "\n")
            