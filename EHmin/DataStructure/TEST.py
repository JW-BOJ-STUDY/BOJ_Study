from sys import stdin

input = stdin.readline

notation = list(input().strip())
my_stack = []
dic = {}
# index = 0
is_break = False
# temp = ""


# while ("(" in notation):
#     is_break = False
#     for i in range(len(notation)):
#         if is_break == True:
#             continue
#         elif notation[i] == "(" and notation[i+4] == ")":
#                 dic[str(index)] = notation[i+1] + notation[i+3] + notation[i+2]
#                 notation = notation.replace(notation[i:i+5],str(index))
#                 index += 1
#                 is_break = True

# while ("*" in notation or "/" in notation ):
#     is_break = False
#     for i in range(len(notation)):
#         if is_break == True:
#             continue
#         elif notation[i] == "/" or notation[i] == "*":
#             dic[str(index)] = notation[i-1] + notation[i+1] + notation[i]
#             notation = notation.replace(notation[i-1:i+2], str(index))
#             index += 1
#             is_break = True
#             print(notation)

# while ("+" in notation or "-" in notation):
#     is_break = False
#     for i in range(len(notation)):
#         if is_break == True:
#             continue
#         elif notation[i] == "+" or notation[i] == "-":
#             dic[str(index)] = notation[i-1] + notation[i+1] + notation[i]
#             notation = notation.replace(notation[i-1:i+2], str(index))
#             index += 1
#             is_break = True



# for i in range(index-1,-1,-1):
#     notation = notation.replace(str(i), dic[str(i)]) 

## 이제 각각의 케이스에 대한건 전부 해결했다. ()안에 여러개가 들어가는 경우 어떻게 해줄것인지에 대한 고민이 필요
# print(notation)
5


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
            print(list)
            if index == 11:
                break
        else:
            index += 1
            print(index)
            
            
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

def break_bracket(notation):
    while ("(" in notation):
        is_break = False
    for i in range(len(notation)):
        if is_break == True:
            continue
        elif notation[i] == "(" and notation[i+4] == ")":
                dic[str(index)] = notation[i+1] + notation[i+3] + notation[i+2]
                notation = notation.replace(notation[i:i+5],str(index))
                index += 1
                is_break = True
    return notation


add_bracket_for_Symbol(notation, "*", "/")
add_bracket_for_Symbol(notation, "+", "-")
#notation을 array로 바꾸어주고,
notation = break_bracket(notation)
# for i in range(index-1,-1,-1):
#     notation = notation.replace(str(i), dic[str(i)]) 
print(notation)
