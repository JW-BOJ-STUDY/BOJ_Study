from sys import stdin, stdout

input = stdin.readline
print = stdout.write

########################################################################
class DList:
    
    class Node:
        def __init__(self, item, prev, link): 
            self.item = item
            self.prev = prev 
            self.next = link  

    def __init__(self):  
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def Dl_size(self):
        return self.size

    def insert_after(self, p, item):  
        t = p.next 
        n = self.Node(item, p, t)  
        t.prev = n  
        p.next = n  
        self.size += 1
        return n

    def delete(self, x): 
        f = x.prev 
        r = x.next 
        f.next = r  
        r.prev = f  
        self.size -= 1
        return f 

    def print_list(self):
        p = self.head.next
        while p != self.tail:
            print(p.item)
            p = p.next  

##########################################################################

sentence = DList()
input_sentence = list(input().strip())
present_node = None
for word in input_sentence:
    if sentence.Dl_size()== 0:
        present_node = sentence.insert_after(sentence.head, word)
    else:
        present_node = sentence.insert_after(present_node, word)

        
for _ in range(int(input())):
    order = input().strip().split()
    if order[0] == "L":
        if present_node.prev == None:
            _
        else:
            present_node = present_node.prev
    elif order[0] == "D":
        if present_node.next == sentence.tail:
            _
        else:
            present_node =present_node.next
    elif order[0] == "B":
        if present_node.prev == None:
            _
        else:
            present_node = sentence.delete(present_node)
    else:
        present_node = sentence.insert_after(present_node, order[1])

        
sentence.print_list()