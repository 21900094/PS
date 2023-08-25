n=int(input())
for i in range(0,n):
    rep,stri=input().split()
    rep=int(rep)
    n_list=list(map(str,stri))
    for j in range(0,len(stri)):
        for p in range(0,rep):
            print(n_list[j],end='')
    print()