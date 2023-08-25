num=int(input())
stack=list()
for i in range(num):
    insert=int(input())
    if insert==0 :
        top=stack.pop()
    else :
        stack.append(insert)
print(sum(stack))