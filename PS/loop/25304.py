sum=int(input())
check=0
number=int(input())
price=list()
n=list()
for i in range(0,number):
    prices,num=input().split()
    price.append(int(prices))
    n.append(int(num))
    check+=(price[i]*n[i])
if sum==check :
    print("Yes")
else : 
    print("No")
    
