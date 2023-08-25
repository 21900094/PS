import sys
num=int(input())
strings=list()
count=0
for i in range(num):
    str=sys.stdin.readline()
    for j in range(len(str)):
        strings.append(str[j])
    for p in range(len(strings)):
        top=strings.pop()
        if top==")":
            count=0
