x,y,w,h=map(int,input().split())
left=x
right=w-x
top=y
bottom=h-y
p_list=[left,right,top,bottom]
print(min(p_list))