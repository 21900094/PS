import sys
num=int(input())
queue=list()

for i in range(num):
    command=list(map(str,input().split()))
    if command[0]=="push" :
        queue.append(int(command[1]))
    elif command[0]=='front':
        if len(queue) ==0 :
            print(-1)
        else :
            print(queue[0])
    elif command[0]=="back":
        if len(queue) ==0 :
            print(-1)
        else :
            print(queue[len(queue)-1])
    elif command[0]=="pop":
        if len(queue)==0:
            print(-1)
        else :
            print(queue.pop(0))
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        if len(queue)==0:
            print(1)
        else :
            print(0)