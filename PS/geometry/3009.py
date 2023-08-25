x_list=list()
y_list=list()
for i in range(0,3):
    x,y=map(int,input().split())
    x_list.append(x)
    y_list.append(y)
for i in range(0,3):
    if x_list.count(x_list[i])==1:
        x_list.append(x_list[i])
    if y_list.count(y_list[i])==1:
        y_list.append(y_list[i])
print(str(x_list[3])+' '+str(y_list[3]))