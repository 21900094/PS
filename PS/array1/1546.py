num=int(input())
sum=0
n_list=list(map(int,input().split()))
item=max(n_list)
for i in range(0,len(n_list)):
    n_list[i]=n_list[i]/item*100
    sum+=n_list[i]

print(float(sum/num))