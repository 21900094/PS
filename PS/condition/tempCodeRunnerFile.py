a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
item=[a,b,c]
if a==b and b==c :
    print(10000+a*1000)
elif a==b or a==c or a==c :
    if a==b :
        print(1000+100*a)
    if a==c :
        print(1000+100*a)
    if c==b :
        print(1000+100*b)
else :
    print(max(item)*100)