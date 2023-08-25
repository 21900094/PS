h,m=input().split()
h=int(h)
m=int(m)
if m>=45 :
    m-=45
elif m<45 :
    m=m+15
    if h==0 :
        h=23
    elif h!=0 :
        h-=1
print(str(h)+" "+str(m))