first,second=input().split()
first=list(first)
second=list(second)
first.reverse()
second.reverse()

first_r=''.join(first)
second_r=''.join(second)
fircp=int(first_r)
seccp=int(second_r)
if fircp>=seccp :
    print(fircp)
else :
    print(seccp)