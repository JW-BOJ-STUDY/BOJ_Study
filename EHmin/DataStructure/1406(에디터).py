from sys import stdin, stdout

input = stdin.readline
print = stdout.write

sentence = list(input().strip())
cursor_position = len(sentence) - 1

def move_cursor_left(cursor_position):
    if(cursor_position == -1):
        return cursor_position
    else:
        cursor_position = cursor_position - 1
        return cursor_position
        
def move_cursor_right(cursor_position):
    if(cursor_position == len(sentence)):
        return cursor_position
    else:
        cursor_position = cursor_position + 1
        return cursor_position
        
def delete(cursor_position):
    if(cursor_position == -1):
        return cursor_position
    else:
        del sentence[cursor_position]
        cursor_position = cursor_position - 1
        return cursor_position
        
def add(cursor_position,x):
    cursor_position = cursor_position + 1
    if cursor_position == len(sentence):
        sentence.append(x)
        return cursor_position
    else:
        sentence.insert(cursor_position,x)
        return cursor_position

for _ in range(int(input())):
    order = input().strip().split()
    if order[0] == "L":
        cursor_position = move_cursor_left(cursor_position)
        # print(sentence,cursor_position)
    elif order[0] == "D":
        cursor_position = move_cursor_right(cursor_position)
        # print(sentence, cursor_position)
    elif order[0] == "B":
        cursor_position = delete(cursor_position)
        # print(sentence, cursor_position)
    else:
        cursor_position = add(cursor_position,order[1])
        # print(sentence, cursor_position)
        
for word in sentence:
    print(word)


