n=int(input())
for i in range(0,n,1):
    for j in range(0,n-i-1,1):
        print(" ",end='')
    for p in range(0,i+1,1):
        print("*",end='')
    print()
