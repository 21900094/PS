num=int(input())
n_list=list()
for i in range(0,num):
    a=int(input())
    n_list.append(a)
n_list.sort()

for i in range(num):
    print(n_list[i])