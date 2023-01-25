from sys import stdin
input = stdin.readline

arr = input().strip()
suffix = []

for i in range(len(arr)):
    suffix.append(arr[i:])
suffix.sort()

for i in range(len(arr)):
    print(suffix[i])
    