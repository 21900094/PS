n_list=list()
for i in range(0,28,1):
    a=int(input())
    n_list.append(a)
for i in range(1,31,1):
    if i not in n_list :
        print(i)