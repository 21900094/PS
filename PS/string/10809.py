str=input()
a_list=str
for i in range(0,26,1):
    if chr(97+i) in a_list :
        print(a_list.find(chr(97+i)),'',end='')
    else :
        print("-1 ",end='')