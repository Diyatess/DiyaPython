n=int(input("enter the limit:"))
for i in range(0,n+1):

    for j in range(1,i+1):
        x=i*j
        print(x,end=" ")
    print()