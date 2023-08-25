hour,minute=input().split()
extra=int(input())
hour=int(hour)
minute=int(minute)

minute+=extra
if minute>=60:
    hour+=(minute//60)
    minute=minute%60

if hour>=24 :
    hour-=24

print(str(hour)+" "+str(minute))