import sys
num=int(input())
for i in range(0,num,1):
    a,b=sys.stdin.readline().rstrip().split()
    a=int(a)
    b=int(b)
    print(a+b)