n_list=list()
for i in range(0,10):
    a=int(input())
    if (a%42) not in n_list :
        n_list.append(a%42)
print(len(n_list))