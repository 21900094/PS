mid=0
while True:
    a,b,c=map(int,input().split())
    l_list=[a,b,c]
    max=max(l_list)
    min=min(l_list)

    if (a!=max) and (a!=min) :
        mid=a
    elif (b != max) and (b != min) :
        mid=b
    elif (c!= max) and (c!=min) :
        mid=c

    if mid+min<=max :
        print("Invalid")

    elif  max==min and max==mid and mid==min and max==0 :
        break
    else :
        if max==mid and mid==min :
            print("Equilateral")
        elif max==mid or mid==min :
            print("Isosceles")
        else :
            print("Scalene")

