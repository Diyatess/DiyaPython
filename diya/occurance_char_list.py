n=int(input("enter the size of list"))
print("enter the elements")
l=[]
count=0
for i in range (0,n):
    ele=input()
    l.append(ele)
for i in l:
    for j in i:
        if j=='a':
            count+=1
print(count)
