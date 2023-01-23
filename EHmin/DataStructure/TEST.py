from sys import stdin

input = stdin.readline

notation = list(input().strip())
my_stack = []
dic = {}
# index = 0
is_break = False

def add_bracket_for_Symbol(list, Symbol1, Symbol2 ):
    index = 0 
    while True:
        if index == len(list):
            break 
        elif list[index] == Symbol1 or list[index] == Symbol2:
            list.insert(find_left_index(list, index),"(")
            index += 1
            list.insert(find_right_index(list, index),")")
            index += 1
        else:
            index += 1
            
            
def find_left_index(list, index):
    my_stack = []
    i = 1
    if list[index - i] == ")":
        my_stack.append(list[index - i])
        while len(my_stack) != 0:
            i += 1
            if list[index - i] == ")":
                my_stack.append(list[index - i])
            elif list[index - i] == "(":
                my_stack.pop()
    return index - i 

def find_right_index(list, index):
    my_stack = []
    i = 1
    if list[index + i] == "(":
        my_stack.append(list[index + i])
        while len(my_stack) != 0:
            i += 1
            if list[index + i] == "(":
                my_stack.append(list[index + i])
            elif list[index + i] == ")":
                my_stack.pop()
    return index + i + 1

def break_bracket(notation, dic):
    index = 0 
    while len(notation) != 1:
        is_break = False
        for i in range(len(notation)):
            if is_break == True:
                continue
            # elif notation[i] == "(" and notation[i+2] == ")":
            #         notation = notation.replace(notation[i:i+3],notation[i+1])
            #         is_break = True
            elif notation[i] == "(" and notation[i+4] == ")":
                    dic[str(index)] = notation[i+1] + notation[i+3] + notation[i+2]
                    notation = notation.replace(notation[i:i+5],str(index))
                    index += 1
                    is_break = True
            elif notation[i] == "+" or notation[i] == "-":
                if notation[i-1] != ")" and notation[i+1] != "(":
                    dic[str(index)] = notation[i-1] + notation[i+1] + notation[i]
                    notation = notation.replace(notation[i-1:i+2],str(index))
                    index += 1
                    is_break = True
        print(notation)            
            
    return notation# 해당 파트를 재귀로 짜주어야 할거같은데.. 안그러면 너무 많이 돌거같아


# def break_bracket(list, dic):
#     index = 05

def change_notation(notation, dic_index):
    for _ in range(len(notation)//2):
        dic[str(dic_index)] = notation[0] + notation[2] + notation[1]
        notation = notation.replace(notation[0:3],str(dic_index))
        dic_index += 1
        print(notation)
    return notation
        


add_bracket_for_Symbol(notation, "*", "/")
# add_bracket_for_Symbol(notation, "+", "-")
#notation을 array로 바꾸어주고,
notation = ''.join(word for word in notation)
notation = break_bracket(notation, dic)

# notation = change_notation(notation, len(dic))





for i in range(len(dic)-1,-1,-1):
    notation = notation.replace(str(i), dic[str(i)]) 

print(notation)
