l1=[1,2,4,5,7,8]
l2=[8,9,5,6,2,3]
a= len(l1)==len(l2)
print(a,"the length are equal")
b=sum(l1)==sum(l2)
print(b)
count=0
for x in l1:
    for y in l2:
        if(x==y):
            count=1
if(count==1):
    print("there is common elements")
else:
    print("there is no common elements")

