number,min=map(int,input().split())
n_list=list(map(int,input().split()))
arr=list()
for i in range(len(n_list)):
    if n_list[i]<min:
        arr.append(n_list[i])
for j in range(len(arr)):
    print(arr[j],'',end='')