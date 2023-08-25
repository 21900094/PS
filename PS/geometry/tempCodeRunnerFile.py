while True:
    a,b,c=map(int,input().split())
    if a==b and a==c and a==0 :
        break
    else :
        if a>b and a>c :
            if b+c<=a :
                print("Invalid")
        elif b>c and b>a :
            if a+c<=b:
                print("Invalid")
        elif c>a and c>b :
            if a+b<=c :
                print("Invalid")
        elif a==b and a==c :
            print("Equilateral")
        elif a==b or a==c or b==c :
            print("Isosceles")
        else :
            print("Scalene")

        