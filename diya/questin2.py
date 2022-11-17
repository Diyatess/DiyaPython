a=int(input("Enter the limit"))
t1=0
t2=1
i=3
while(i<=a):
    next=t1+t2
    t1=t2
    t2=next
    i += 1
    if next%12==0:
        print(next)