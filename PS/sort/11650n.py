num=int(input())
temp=0
arr=[[0] for i in range(2) for j in range(num)]
for p in range(num):
    x,y=map(int,input().split())
    arr[p][0]=x
   
for i in range(0,num-1):
    for j in range(0,num-1-i):
        if arr[j][0]>arr[j+1][0]:
            temp=arr[j][0]
            arr[j][0]=arr[j+1][0]
            arr[j+1][0]=temp
            temp=arr[j][1]
            arr[j][1]=arr[j+1][1]
            arr[j+1][1]=temp
        elif arr[j][0]==arr[j+1][0]:
            if arr[j][1]>arr[j+1][1]:
                temp=arr[j][0]
                arr[j][0]=arr[j+1][0]
                arr[j+1][0]=temp
                temp=arr[j][1]
                arr[j][1]=arr[j+1][1]
                arr[j+1][1]=temp
for i in range(0,num):
    print(arr[i][0]+" "+arr[i][1])
