from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n = int(input())

for i in range(n):
    sentence = input().split()
    for word in sentence:
        word = list(word)
        while(len(word) != 0):
            print(word.pop())
        print(" ")
    print("\n")

