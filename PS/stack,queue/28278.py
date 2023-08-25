import sys
stack=list()
num=int(input())
for i in range(num):
    command=sys.stdin.readline().split()
    if command[0]=="1":
        stack.append(command[1])
    elif command[0]=="2":
        if len(stack)==0 :
            print(-1)
        else:
            top=stack.pop()
            print(top)
    elif command[0]=="3":
        print(len(stack))
    elif command[0]=="4":
        if len(stack)==0:
            print(1)
        else :
            print(0)
    elif command[0]=="5":
        if len(stack)==0:
            print(-1)
        else :
            top=stack[-1]
            print(top)




